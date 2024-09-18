from django.test import TestCase, override_settings
from newspaper.forms import RedactorCreateForm, RedactorUpdateForm
from newspaper.models import Redactor


class FormsTests(TestCase):
    def setUp(self):
        self.redactor = Redactor.objects.create_user(
            username="existing_redactor",
            years_of_experience=3,
            first_name="Existing",
            last_name="Redactor",
            password="Test12345"
        )

    @override_settings(AUTH_PASSWORD_VALIDATORS=[])
    def test_redactor_creation_form_with_years_of_experience_is_valid(self):
        form_data = {
            "username": "test_redactor",
            "years_of_experience": 5,
            "first_name": "Test",
            "last_name": "Redactor",
            "password1": "Test123",
            "password2": "Test123",
        }
        form = RedactorCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    @override_settings(AUTH_PASSWORD_VALIDATORS=[])
    def test_redactor_update_form_is_valid(self):
        form_data = {
            "username": "updated_redactor",
            "years_of_experience": 7,
            "first_name": "Updated",
            "last_name": "Redactor",
        }
        form = RedactorUpdateForm(data=form_data, instance=self.redactor)
        self.assertTrue(form.is_valid())
