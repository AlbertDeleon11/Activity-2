from django.shortcuts import render
from django.views.generic import TemplateView

class Homepageview(TemplateView):
    template_name = 'app/Home.html'

class Contactpageview(TemplateView):
    template_name = 'app/Contact.html'
class Aboutpageview(TemplateView):
    template_name = 'app/About.html'
