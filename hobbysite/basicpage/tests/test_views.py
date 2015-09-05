from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from basicpage.views import home_page
from basicpage.views import about_page
from basicpage.views import anno_page


class BasicPageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        #print(response.content)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>DC Maxecuters', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
        
    def test_home_page_renders_from_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
       
    def test_about_url_resolves_to_about_page_view(self):
        found = resolve('/about')
        self.assertEqual(found.func, about_page)
        
    def test_about_page_renders_from_template(self):
        response = self.client.get('/about')
        self.assertTemplateUsed(response, 'about.html')
        
    def test_anno_url_resolves_to_anno_page_view(self):
        found = resolve('/anno')
        self.assertEqual(found.func, anno_page)
        
    def test_anno_page_renders_from_template(self):
        response = self.client.get('/anno')
        self.assertTemplateUsed(response, 'anno.html')
        
        
