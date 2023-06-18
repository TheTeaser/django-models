from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import Snack

# Create your tests here.


class SnacksTest(TestCase):
    def setUp(self):
        reviewer = get_user_model().objects.create(username="tester", password="tester")
        Snack.objects.create(name="tester", purchaser=reviewer)

    def test_snack_list_status(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_list_response(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "base.html")

    def test_detail_page_status(self):
        url = reverse("snack_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        url = reverse("snack_detail", args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, "base.html")

    def test_detail_page_context(self):
        url = reverse("snack_detail", args=(1,))
        response = self.client.get(url)
        snack_detail = response.context["snack"]
        self.assertEqual(snack_detail.name, "tester")
        self.assertEqual(snack_detail.purchaser.username, "tester")
