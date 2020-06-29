from django.shortcuts import render
import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse("Oh henlo, Django!")


def henlo_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using the regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.

    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Freeeind"

    content = "Henlo there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)
