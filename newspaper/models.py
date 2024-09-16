from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ("username", )

    def get_absolute_url(self):
        return reverse("newspaper:redactor-detail", args=[str(self.pk)])


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField()
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE)
    publishers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="newspapers"
    )

    class Meta:
        ordering = ("published_date", )
