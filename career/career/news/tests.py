from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import News
from ..companies.models import Company

User = get_user_model()

class NewsViewsTestCase(TestCase):

    def setUp(self):
        # Create a test user, company, and news article
        self.user = User.objects.create_user(
            username='testcompany',
            email='testcompany@example.com',
            password='testpass123',
            is_company=True
        )
        self.company = Company.objects.create(
            user=self.user,
            name="Test Company",
            description="A test company"
        )
        self.news_article = News.objects.create(
            company=self.company,
            title="Test News",
            content="This is a test news article.",
            date_posted="2023-01-01"
        )
        self.client.login(username='testcompany', password='testpass123')

    def test_news_create_view(self):
        response = self.client.get(reverse('news:create-news'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news_form.html')

        # Test post request (creating a news article)
        response = self.client.post(reverse('news:create-news'), {
            'title': 'New Test News',
            'content': 'This is another test news article.',
            'date_posted': '2023-01-02'
        })
        self.assertRedirects(response, reverse('news:company_news_list'))
        self.assertTrue(News.objects.filter(title='New Test News').exists())

    def test_company_news_list_view(self):
        response = self.client.get(reverse('news:company_news_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/company_news_list.html')
        self.assertIn(self.news_article, response.context['news_articles'])

    def test_news_delete_view(self):
        response = self.client.get(reverse('news:delete-news', kwargs={'pk': self.news_article.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news_confirm_delete.html')

        # Test delete request
        response = self.client.post(reverse('news:delete-news', kwargs={'pk': self.news_article.pk}))
        self.assertRedirects(response, reverse('news:company_news_list'))
        self.assertFalse(News.objects.filter(pk=self.news_article.pk).exists())

    def test_news_list_view(self):
        response = self.client.get(reverse('news:news-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news_list.html')
        self.assertIn(self.news_article, response.context['news_articles'])

    def test_news_detail_view(self):
        response = self.client.get(reverse('news:news-detail', kwargs={'pk': self.news_article.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news_detail.html')
        self.assertEqual(response.context['news_article'], self.news_article)

