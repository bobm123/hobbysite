from django.test import TestCase
from django.core.exceptions import ValidationError
from newsletter.models import Newsletter
from django.template.defaultfilters import slugify


class NewsletterModelTest(TestCase):

    def test_slug_based_on_name(self):
        newsletter = Newsletter(name="MaxFax 2015-1")
        newsletter.save()
        self.assertEqual(newsletter.slug, slugify("MaxFax 2015-1"))