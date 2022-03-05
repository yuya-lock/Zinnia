from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

class HomeView(TemplateView):
    template_name = 'home.html'