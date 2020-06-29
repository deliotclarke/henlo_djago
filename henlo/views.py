from django.shortcuts import render
import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse("Oh henlo, Django!")


def henlo_there(request, name):
    return render(
        request,
        'henlo/henlo_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
