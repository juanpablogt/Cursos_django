from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView   

class HomePageView(TemplateView):
    template_name = 'home.html'

class My_codesPageView(TemplateView):
    template_name = 'my_codes.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'