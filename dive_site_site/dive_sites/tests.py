from django.test import SimpleTestCase
from django.urls import reverse

class DiveSiteTest(SimpleTestCase):

    def test_home_page(self):
        url = reverse('home')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_dive_site_template(self):
        url = reverse('dive_site_details')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'dive_site_details')
        self.assertTemplateUsed(response, 'base.html')
