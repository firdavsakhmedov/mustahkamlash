from re import template
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class TelegramPageView(TemplateView):
    template_name = 'telegram.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'