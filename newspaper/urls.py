from django.urls import path

from .views import (
    index,
    RedactorListView,
    RedactorCreateView,
    RedactorDetailView,
    RedactorsDeleteView,
    RedactorUpdateView,
    NewspaperListView,
    NewspaperCreateView,
)


urlpatterns = [
    # Redactors
    path("", index, name="index"),
    path("redactors/",
         RedactorListView.as_view(), name="redactor-list"),
    path("redactors/create",
         RedactorCreateView.as_view(), name="redactor-create"),
    path(
        "redactors/<int:pk>/",
        RedactorDetailView.as_view(), name="redactor-detail"
    ),
    path("redactors/<int:pk>/delete/",
         RedactorsDeleteView.as_view(),
         name="redactor-delete"
         ),
    path("redactors/<int:pk>/update/",
         RedactorUpdateView.as_view(),
         name="redactor-update"
         ),
    # Newspapers
    path("newspapers/", NewspaperListView.as_view(),
         name="newspaper-list"),
    path("newspapers/create",
         NewspaperCreateView.as_view(), name="newspaper-create"),
]


app_name = "newspaper"
