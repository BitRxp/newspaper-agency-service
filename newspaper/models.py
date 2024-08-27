from django.contrib.auth.models import AbstractUser
from django.db import models

from newspaper_agency_service import settings


class Topic(models.Model):
    name = models.CharField(max_length=255)


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField()

    class Meta:
        ordering = ("username", )


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
