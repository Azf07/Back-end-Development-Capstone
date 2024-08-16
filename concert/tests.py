from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from concert.models import Concert, ConcertAttending

class ConcertViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.concert = Concert.objects.create(
            concert_name="Test Concert",
            duration="02:00:00",
            city="Test City",
            date="2023-08-15"
        )

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_concerts_view_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('concerts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'concerts.html')

    def test_concerts_view_unauthenticated(self):
        response = self.client.get(reverse('concerts'))
        self.assertEqual(response.status_code, 302)  # Redirect to login
        self.assertRedirects(response, reverse('login'))

    def test_concert_detail_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('concert_detail', args=[self.concert.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'concert_detail.html')
        self.assertContains(response, self.concert.concert_name)
