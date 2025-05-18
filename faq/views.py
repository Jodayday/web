from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class FAQListView(TemplateView):
    template_name = 'faq.html'
