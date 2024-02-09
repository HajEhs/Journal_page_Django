from django.test import TestCase
from django.shortcuts import reverse
from .models import Journal, Note

class JournalListViewTest(TestCase):
    def setUp(self):
        self.journal_page = Journal.objects.create(text='banana', name='Z', number=20)

    def test_journal_list_view_ulr(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)  # AssertaionError: 404 -> Page not found

    def test_journal_list_name(self):
        response = self.client.get(reverse("PageList"))
        self.assertEqual(response.status_code, 200)

    def test_journal_list_page(self):
        response = self.client.get(reverse("About"))
        self.assertContains(response, self.journal_page.text)


