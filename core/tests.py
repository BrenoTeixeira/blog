from django.test import TestCase


class HomePageViewTests(TestCase):

	def setUp(self):
		self.resp = self.client.get('/')

	def test_GET_homepage(self):
		self.assertEqual(self.resp.status_code, 200)

	def test_template_used(self):
		self.assertTemplateUsed(self.resp, 'core/home.html')
