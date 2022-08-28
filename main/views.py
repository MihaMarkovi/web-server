from django.shortcuts import render
from django.views import generic


class Main(generic.TemplateView):
    template_name = 'main/index.html'
