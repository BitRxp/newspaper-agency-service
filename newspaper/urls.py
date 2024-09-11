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
    NewspaperDetailView,
    NewspaperUpdateView,
    NewspaperDeleteView,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
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
    path("newspapers/<int:pk>/",
         NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("newspapers/<int:pk>/update/",
         NewspaperUpdateView.as_view(), name="newspaper-update"),
    path("newspapers/<int:pk>/delete/",
         NewspaperDeleteView.as_view(),
         name="newspaper-delete"
         ),

    # Topics
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list",
    ),
    path("topics/create",
         TopicCreateView.as_view(), name="topic-create"),
    path("topics/<int:pk>/update/",
         TopicUpdateView.as_view(), name="topic-update"),
    path("topics/<int:pk>/delete/",
         TopicDeleteView.as_view(),
         name="topic-delete"
         ),
]


app_name = "newspaper"
