from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect 
from django.shortcuts import render
from django.views.generic import TemplateView
from .tokenizing import *

class HomeView(TemplateView):
    template_name = "home.html"

def validate(request):
    if request.method == 'POST':
        username = request.POST["user"]

        dict = {
            'username' : tokenization(username)
        }
        
        return render(request,'result.html',dict)
