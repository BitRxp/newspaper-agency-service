from django.contrib.auth import get_user_model
from django.test import TestCase
from newspaper.models import Topic, Newspaper


class ModelTests(TestCase):
    def test_topic_str(self):
        """Test the Topic string representation"""
        topic = Topic.objects.create(name="Politics")
        self.assertEqual(str(topic), topic.name)

    def test_redactor_str(self):
        """Test the Redactor string representation"""
        redactor = get_user_model().objects.create_user(
            username="test_redactor",
            password="Test12345",
            first_name="Test",
            last_name="Redactor"
        )
        self.assertEqual(
            str(redactor),
            f"{redactor.username}"
        )

    def test_create_redactor_with_years_of_experience(self):
        """Test creating a redactor with years of experience"""
        username = "test_redactor"
        password = "Test12345"
        years_of_experience = 5
        redactor = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience
        )
        self.assertEqual(redactor.username, username)
        self.assertEqual(redactor.years_of_experience, years_of_experience)
        self.assertTrue(redactor.check_password(password))

    def test_newspaper_str(self):
        """Test the Newspaper string representation"""
        topic = Topic.objects.create(name="Politics")
        newspaper = Newspaper.objects.create(
            title="Breaking News",
            content="Important content",
            published_date="2024-09-15",
            topic=topic
        )
        self.assertEqual(str(newspaper), newspaper.title)
