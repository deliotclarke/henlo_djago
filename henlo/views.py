from django.shortcuts import render
import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "henlo/home.html")


def about(request):
    return render(request, "henlo/about.html")


def contact(request):
    return render(request, "henlo/contact.html")


def henlo_there(request, name):
    return render(
        request,
        'henlo/henlo_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
