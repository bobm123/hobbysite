from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from newsletter.views import browse_by_year


class NewsletterPageTest(TestCase):

    def test_newsletter_url_resolves_to_newsletter_view(self):
        found = resolve('/maxfax')
        self.assertEqual(found.func, browse_by_year)

    def test_newsletter_uses_template(self):
        response = self.client.get('/maxfax')
        self.assertTemplateUsed(response, 'newsletter.html')
        
    def test_page_shows_newsletter(self):
        response = self.client.get('/maxfax')
        self.assertEqual(response.status_code, 200)
