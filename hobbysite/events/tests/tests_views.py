from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from basicpage.views import home_page


class EventsPageTest(TestCase):

    def test_can_navigate_to_events(self):
        response = self.client.get('/events')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events.html')
        self.assertIn(b'<title>DC Maxecuters-Events</title>', response.content)
        
    def test_page_shows_comming_events(self):
        response = self.client.get('/events')
        self.assertIn(b'January', response.content)
        self.assertIn(b'December', response.content)
