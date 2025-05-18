from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class DownloadsView(TemplateView):
    template_name = 'downloads.html'
