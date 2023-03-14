from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect 
from django.shortcuts import render
from django.views.generic import TemplateView
from .tokenizing import *

class HomeView(TemplateView):
    template_name = "home.html"

class crawlerView(TemplateView):
    template_name = "crawler.html"

def validate(request):
    if request.method == 'POST':
        username = request.POST["user"]

        dict = {
            'username' : tokenization(username)
        }
        
        return render(request,'result.html',dict)

def crawler(request):
    return render(request,'crawler.html')