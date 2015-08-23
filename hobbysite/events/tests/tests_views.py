from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from events.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        #print(response.content)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>DC Maxecuters', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
        
    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
       
    def test_can_navigate_to_events(self):
        response = self.client.get('/events')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events.html')
        self.assertIn(b'<title>DC Maxecuters-Events</title>', response.content)
        

class EventsPageTest(TestCase):

    def test_page_shows_comming_events(self):
        response = self.client.get('/events')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'January', response.content)
        self.assertIn(b'December', response.content)

