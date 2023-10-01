from django.urls import path
from . import views
from .views import Registraion, HomePageView, CreateOffer


urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('create-offer/', CreateOffer.as_view(), name='create_offer'),
    path("signup/", Registraion.as_view(), name="signup"),
    path("test/", views.test, name="test"),
]