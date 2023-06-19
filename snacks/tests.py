from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack


class SnacksTest(TestCase):
    def setUp(self):
        reviewer = get_user_model().objects.create(username="tester", password="tester")
        self.purchaser = reviewer
        self.snack = Snack.objects.create(name="tester", purchaser=reviewer)

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
        url = reverse("snack_detail", args=(self.snack.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        url = reverse("snack_detail", args=(self.snack.pk,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, "base.html")

    def test_detail_page_context(self):
        url = reverse("snack_detail", args=(self.snack.pk,))
        response = self.client.get(url)
        snack_detail = response.context["snack"]
        self.assertEqual(snack_detail.name, "tester")
        self.assertEqual(snack_detail.purchaser.username, "tester")

    def test_create_view(self):
        obj = {
            "name": "test2",
            "purchaser": self.purchaser.id,
            "description": "info...",
        }

        url = reverse("snack_create")
        response = self.client.post(path=url, data=obj, follow=True)
        self.assertEqual(len(Snack.objects.all()), 2)

    def test_update_view(self):
        obj = {
            "name": "test2",
            "purchaser": self.purchaser.id,
            "description": "info...",
        }

        url = reverse("snack_update", args=(self.snack.pk,))
        response = self.client.post(path=url, data=obj, follow=True)
        self.assertRedirects(response, reverse("snack_list"))

    def test_delete_view(self):
        url = reverse("snack_delete", args=(self.snack.pk,))
        response = self.client.post(path=url, follow=True)
        self.assertRedirects(response, reverse("snack_list"))

    def test_str_method(self):
        self.assertEqual(str(self.snack), "tester")

    def test_create_response(self):
        url = reverse("snack_create")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_create.html")
        self.assertTemplateUsed(response, "base.html")

    def test_update_response(self):
        url = reverse("snack_update", args=(self.snack.pk,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_update.html")
        self.assertTemplateUsed(response, "base.html")

    def test_delete_response(self):
        url = reverse("snack_delete", args=(self.snack.pk,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_delete.html")
        self.assertTemplateUsed(response, "base.html")
