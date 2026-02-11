from django.test import TestCase
from django.urls import reverse
from .utils import add


class AddFunctionTestCase(TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)


class HomePageTestCase(TestCase):
    def test_home_page_contains_homepage_text(self):
        response = self.client.get(reverse('notes:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Homepage')
