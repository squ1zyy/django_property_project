from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, RealEstate

class SingUpUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=55, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length= 55, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password_1 = forms.CharField(max_length=70)
    password_2 = forms.CharField(max_length=70)
    # avatar = forms.ImageField(widget=forms.ImageInput(attrs={'class'}))

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password_1', 'password_2')

class PropertiesForm(forms.ModelForm):
    class Meta:
        model = RealEstate
        fields = ['title', 'description', 'price', 'location']