"""
All major functions in project_henlo
"""

from datetime import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from henlo.forms import LogMessageForm
from henlo.models import LogMessage

# Create your views here.


class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


def about(request):
    """renders about page on request"""
    return render(request, "henlo/about.html")


def contact(request):
    """renders contact page on request"""
    return render(request, "henlo/contact.html")


def henlo_there(request, name):
    """renders henlo there page with name placed in url and timestamp of instantiation"""
    return render(
        request,
        'henlo/henlo_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )


def log_message(request):
    """function posting log message model after user creation and redirecting user to home to view log messages"""
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "henlo/log_message.html", {"form": form})
