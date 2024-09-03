from django.urls import path

from .views import (
    index,
    RedactorListView,
    RedactorCreateView,
    RedactorDetailView
)


urlpatterns = [
    path("", index, name="index"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactors/create", RedactorCreateView.as_view(), name="redactor-create"),
    path(
        "redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"
    ),
]


app_name = "newspaper"
