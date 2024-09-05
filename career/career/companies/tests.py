from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Company
from ..listings.models import JobListing

User = get_user_model()

class CompanyViewsTestCase(TestCase):

    def setUp(self):
        # Create a test user and company
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
        self.client.login(username='testcompany', password='testpass123')

    def test_company_registration_view(self):
        response = self.client.get(reverse('companies:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/register.html')

    def test_company_login_view(self):
        response = self.client.get(reverse('companies:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/login.html')

    def test_company_detail_view(self):
        response = self.client.get(reverse('companies:company-detail', kwargs={'pk': self.company.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/company_detail.html')

    def test_company_info_view(self):
        response = self.client.get(reverse('companies:company-info', kwargs={'pk': self.company.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/company_info.html')

    def test_company_update_view(self):
        response = self.client.get(reverse('companies:company-update', kwargs={'pk': self.company.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/company_update.html')

    def test_manage_job_listings_view(self):
        response = self.client.get(reverse('companies:manage-job-listings', kwargs={'pk': self.company.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/manage_job_listings.html')

    def test_job_listing_create_view(self):
        response = self.client.get(reverse('companies:job-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/job_create.html')

    def test_job_listing_update_view(self):
        response = self.client.get(reverse('companies:edit-job-listing', kwargs={'pk': self.job_listing.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/edit_job_listing.html')

    def test_job_listing_delete_view(self):
        response = self.client.get(reverse('companies:delete-job-listing', kwargs={'pk': self.job_listing.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/delete_job_listing.html')

    def test_job_listing_monitor_view(self):
        response = self.client.get(reverse('companies:job-listing-monitor', kwargs={'pk': self.job_listing.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/job_listing_monitor.html')
