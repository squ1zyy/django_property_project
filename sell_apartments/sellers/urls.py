from django.urls import path
from . import views
from .views import Registraion, HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path("signup/", Registraion.as_view(), name="signup"),
    path("test/", views.test, name="test"),
]