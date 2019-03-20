# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect

from django.conf import settings




# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'aboutme.html')

def service(request):
    return render(request, 'services.html')

def gallery(request):
    return render(request, 'gallery.html')

def blog(request):
    return render(request, 'blog.html')
def review(request):
    return render(request, 'reviews.html')
def register(request):
    return render(request, 'registration.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contactme/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})







