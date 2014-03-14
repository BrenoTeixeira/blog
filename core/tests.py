from django.test import TestCase
from django.core.urlresolvers import reverse


class HomePageViewTests(TestCase):
    
    def setUp(self):
        self.url = reverse('core:home')
        self.resp = self.client.get(self.url)
    
    def test_GET_homepage(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'core/home.html')

    def test_html5(self):
        self.assertContains(self.resp, '<title>Welcome')
        self.assertContains(self.resp, '<!DOCTYPE HTML>')

