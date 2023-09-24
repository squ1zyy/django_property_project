from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import SingUpUserForm
from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.template import loader
from django.http import HttpResponse
from .models import RealEstate, PictureMain, CustomUser, BlogPost
from django.shortcuts import render
from django.views import View

class HomePageView(View):
    template_name = 'home.html'

    def get(self, request):
        popular_listings = RealEstate.objects.all()
        blog_posts = BlogPost.objects.all()

        context = {
            'popular_listings': popular_listings,
            'blog_posts': blog_posts,
        }

        return render(request, 'home.html', context)


class Registraion(CreateView):
    template_name = 'registration/registration-login-page.html'
    success_url = reverse_lazy('login')
    form_class = SingUpUserForm
    success_message = "Your profile was created successfully"


def test(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['apple', 'banana', 'blueberry'],
    }
    return HttpResponse(template.render(context, request))