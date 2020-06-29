import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from henlo.forms import LogMessageForm
from henlo.models import LogMessage
from django.views.generic import ListView

# Create your views here.


class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


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


def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "henlo/log_message.html", {"form": form})
