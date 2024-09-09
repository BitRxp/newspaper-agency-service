from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from newspaper.forms import RedactorCreateForm, RedactorUpdateForm
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


# RedactorView
class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    paginate_by = 5


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    success_url = reverse_lazy("newspaper:redactor-list")
    form_class = RedactorCreateForm


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.all().prefetch_related("newspapers__topics")


class RedactorsDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("newspaper:redactor-list")


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorUpdateForm
    template_name = "newspaper/redactor_update.html"

    def get_success_url(self) -> str:
        return reverse_lazy(
            "newspaper:redactor-detail",
            kwargs={"pk": self.object.pk}
        )
