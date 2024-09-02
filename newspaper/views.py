from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from newspaper.models import Redactor, Newspaper, Topic


@login_required
def index(request):

    num_redactor = Redactor.objects.count()
    num_newspaper = Newspaper.objects.count()
    num_topic = Topic.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_redactor": num_redactor,
        "num_newspaper": num_newspaper,
        "num_topic": num_topic,
        "num_visits": num_visits + 1,
    }

    return render(request, "newspaper/index.html", context=context)
