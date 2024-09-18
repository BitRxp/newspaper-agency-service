from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from newspaper.models import Topic, Newspaper


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin_password"
        )
        self.client.force_login(self.admin_user)

        self.redactor = get_user_model().objects.create_user(
            username="redactor",
            password="redactor_password",
            years_of_experience=5
        )
        self.topic = Topic.objects.create(name="Politics")
        self.newspaper = Newspaper.objects.create(
            title="Breaking News",
            content="Some content here...",
            published_date="2024-09-15",
            topic=self.topic
        )
        self.newspaper.publishers.add(self.redactor)

    def test_redactor_years_of_experience_listed(self):
        """
        Test that years_of_experience is in list_display on
         redactor admin page
        """
        url = reverse("admin:newspaper_redactor_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.redactor.years_of_experience)

    def test_redactor_detail_years_of_experience_listed(self):
        """
        Test that redactor's years_of_experience
         is in redactor detail admin page
        """
        url = reverse(
            "admin:newspaper_redactor_change",
            args=[self.redactor.id])
        res = self.client.get(url)
        self.assertContains(res, self.redactor.years_of_experience)

    def test_topic_is_registered_in_admin(self):
        """
        Test that Topic model is correctly
         registered in the admin site
        """
        url = reverse("admin:newspaper_topic_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_newspaper_is_registered_in_admin(self):
        """
        Test that Newspaper model is correctly
         registered in the admin site
        """
        url = reverse("admin:newspaper_newspaper_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_newspaper_publishers_listed(self):
        """
        Test that publishers are displayed on
         the Newspaper detail page in admin
        """
        url = reverse(
            "admin:newspaper_newspaper_change",
            args=[self.newspaper.id])
        response = self.client.get(url)
        self.assertContains(response, self.redactor.username)
