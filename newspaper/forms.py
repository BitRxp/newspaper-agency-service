from django.contrib.auth.forms import UserCreationForm
from django import forms

from newspaper.models import Redactor


class RedactorCreateForm(UserCreationForm):
    years_of_experience = forms.IntegerField(
        required=True,
    )

    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )
