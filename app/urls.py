from django.urls import path
from .views import Homepageview, Aboutpageview, Contactpageview

urlpatterns = [
    path('',Homepageview.as_view(),name='Home'),
    path('/Contact', Contactpageview.as_view(), name='Contact'),
    path('/About', Aboutpageview.as_view(), name='About'),]