import json

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import JobListing
from ..companies.models import Company
from ..resume.models import Resume
from ..application.models import Application

User = get_user_model()

class JobListingViewsTestCase(TestCase):

    def setUp(self):
        # Create a test user, company, resume, and job listing
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )
        self.company = Company.objects.create(
            user=self.user,
            name="Test Company",
            description="A test company"
        )
        self.job_listing = JobListing.objects.create(
            company=self.company,
            title="Test Job",
            description="A test job description",
            requirements="Test requirements",
            location="Test location",
            employment_type="Full-time",
            salary_min=50000,
            salary_max=70000
        )
        self.resume = Resume.objects.create(
            user=self.user,
            summary="Test Summary",
            education="Test Education",
            experience="Test Experience",
            skills="Test Skills"
        )
        self.client.login(username='testuser', password='testpass123')

    def test_job_listing_list_view(self):
        response = self.client.get(reverse('listings:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listings/job_list.html')
        self.assertIn(self.job_listing, response.context['jobs'])

    def test_job_listing_detail_view(self):
        response = self.client.get(reverse('listings:detail', kwargs={'pk': self.job_listing.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listings/job_detail.html')
        self.assertEqual(response.context['job'], self.job_listing)

    def test_job_listing_apply_view(self):
        response = self.client.post(reverse('listings:detail', kwargs={'pk': self.job_listing.pk}))
        self.assertRedirects(response, reverse('listings:list'))
        self.assertTrue(Application.objects.filter(user=self.user, job_listing=self.job_listing).exists())

    def test_job_listing_apply_without_resume(self):
        self.resume.delete()  # Remove the resume to test the failure case
        response = self.client.post(reverse('listings:detail', kwargs={'pk': self.job_listing.pk}))
        self.assertRedirects(response, reverse('resume:create-resume'))
        self.assertFalse(Application.objects.filter(user=self.user, job_listing=self.job_listing).exists())

    def test_job_fit_score_view(self):
        response = self.client.post(
            reverse('listings:job-fit-score'),
            data=json.dumps({'job_id': self.job_listing.id}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('score', response.json())
        self.assertIn('text', response.json())

