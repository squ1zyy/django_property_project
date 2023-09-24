from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_str, force_bytes
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.http import Http404

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **kwargs)

    def send_email_confirmation(self, user):
        token = default_token_generator.male_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        domain = get_current_site(None).domain
        
        subject = "Email Confirmation"
        message = render_to_string(
            'email/confirmation_message.txt',
            {'user': user,
             'domain': domain,
             'uid': uid,
             'token': token,
            }
        )
        
        email = EmailMessage(subject, message, to=[user.email])
        email.send()  
    
def confirm_email(self, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = self.get(pk=uid)
    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
        return None

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return user

    return None

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(unique=True, max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "password"]

    def __str__(self):
        return self.email

class RealEstate(models.Model):
    SELLER_CHOICES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    type_estate = models.CharField(max_length=10, choices=SELLER_CHOICES, default='apartment')
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=300)
    location = models.CharField(max_length=300)
    price = models.IntegerField(null=True)
    amount_rooms = models.IntegerField(null=True)

    def real_estate_details(self, request):
        if not request.user.is_seller:
            raise Http404

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_published = models.DateField()
    

class PictureMain(models.Model):
    estate = models.ForeignKey('RealEstate', on_delete=models.CASCADE, related_name='picture')
    photo_main = models.ImageField(upload_to='photos/', blank=False)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description