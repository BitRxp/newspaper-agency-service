from django.shortcuts import render

from newspaper.models import Redactor, Newspaper, Topic


def index(request):
    """View function for the home page of the site."""

    return render(request, "newspaper/index.html")
