from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class UserViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

    def test_registration_view(self):
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_login_view(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_registration_success_view(self):
        response = self.client.get(reverse('users:registration-success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/registration_success.html')

    def test_user_detail_view(self):
        response = self.client.get(reverse('users:user-detail', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'users/user_detail.html')

    def test_user_update_view(self):
        response = self.client.get(reverse('users:user-update', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_update.html')

    def test_password_change_view(self):
        response = self.client.get(reverse('users:password_change'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/password_change.html')
