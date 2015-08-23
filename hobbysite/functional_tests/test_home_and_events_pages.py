from .base import FunctionalTest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):
    
    def test_visitor_can_view_comming_events(self):
        # Don has heard about a cool new model plane site so
        # he goes to check out its homepage
        self.browser.get(self.server_url)

        # He notices the title page mentions the club name
        self.assertIn('DC Maxecuters', self.browser.title)
        
        # He notices a nav button labled 'Events'
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn('Events', navbar.text)
        
        # He goes to the 'Events' button and sees a list of fun meetups
        self.browser.find_element_by_link_text('Events').click()
        self.wait_for(lambda: self.assertIn('Events', self.browser.title))
        #self.wait_for(lambda: self.assertEqual(
        #    self.browser.find_element_by_tag_name('h1').text,
        #    'Events'
        #))
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('JANUARY', page_text)
        self.assertIn('DECEMBER', page_text)
        


