from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.template import loader

# Create your views here.
def editor(request):
    template = loader.get_template('home/editor.html')
    context = {}
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template('home/home.html')
    context = {}
    return HttpResponse(template.render(context, request))