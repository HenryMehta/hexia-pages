from django.shortcuts import render
from django.views.generic import DetailView

from hexia_pages.models import Page
# Create your views here.

class PageView (DetailView):
    model = Page
    #template_name = 'hexia_pages/page.html'