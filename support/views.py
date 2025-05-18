from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class SupportView(TemplateView):
    template_name = 'support.html'
