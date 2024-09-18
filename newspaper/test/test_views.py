from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.models import Topic, Newspaper, Redactor

REDACTOR_URL = reverse("newspaper:redactor-list")
NEWSPAPER_URL = reverse("newspaper:newspaper-list")
TOPIC_URL = reverse("newspaper:topic-list")


class PublicRedactorTests(TestCase):
    def test_login_required_for_redactor_list(self):
        response = self.client.get(REDACTOR_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateRedactorTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.client.force_login(self.user)

    def test_retrieve_redactor_list(self):
        Redactor.objects.create(
            username="testredactor",
            first_name="Test",
            last_name="Redactor"
        )
        response = self.client.get(REDACTOR_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/redactor_list.html")


class PublicNewspaperTests(TestCase):
    def test_login_required_for_newspaper_list(self):
        response = self.client.get(NEWSPAPER_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateNewspaperTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.client.force_login(self.user)
        self.topic = Topic.objects.create(name="Politics")

    def test_retrieve_newspaper_list(self):
        Newspaper.objects.create(
            title="Test News",
            content="Test Content",
            topic=self.topic,
            published_date="2024-09-15"
        )
        response = self.client.get(NEWSPAPER_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/newspaper_list.html")


class PrivateTopicTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.client.force_login(self.user)

    def test_retrieve_topic_list(self):
        Topic.objects.create(name="Politics")
        response = self.client.get(TOPIC_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/topic_list.html")
