from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Resume, Project, Education

User = get_user_model()

class ResumeViewsTestCase(TestCase):

    def setUp(self):
        # Create a test user and associated resume, project, and education
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )
        self.resume = Resume.objects.create(
            user=self.user,
            summary="Test Summary",
            education="Test Education",
            experience="Test Experience",
            skills="Test Skills"
        )
        self.project = Project.objects.create(
            user=self.user,
            title="Test Project",
            description="Test Project Description",
            technologies="Python, Django"
        )
        self.education = Education.objects.create(
            user=self.user,
            degree="Test Degree",
            institution="Test University",
            graduation_year="2023"
        )
        self.client.login(username='testuser', password='testpass123')

    def test_resume_create_view(self):
        response = self.client.get(reverse('resume:create-resume'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resume/resume_create_form.html')

        # Test post request (creating a resume)
        response = self.client.post(reverse('resume:create-resume'), {
            'summary': 'New Test Summary',
            'education': 'New Test Education',
            'experience': 'New Test Experience',
            'skills': 'New Test Skills'
        })
        self.assertRedirects(response, reverse('resume:resume-detail'))
        self.assertTrue(Resume.objects.filter(summary='New Test Summary').exists())

    def test_resume_detail_view(self):
        response = self.client.get(reverse('resume:resume-detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resume/resume_detail.html')
        self.assertEqual(response.context['resume'], self.resume)

    def test_resume_update_view(self):
        response = self.client.get(reverse('resume:update-resume'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resume/resume_update.html')

        # Test post request (updating a resume)
        response = self.client.post(reverse('resume:update-resume'), {
            'summary': 'Updated Summary',
            'education': 'Updated Education',
            'experience': 'Updated Experience',
            'skills': 'Updated Skills'
        })
        self.assertRedirects(response, reverse('resume:resume-detail'))
        self.resume.refresh_from_db()
        self.assertEqual(self.resume.summary, 'Updated Summary')

    def test_project_create_view(self):
        response = self.client.get(reverse('resume:create-project'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_create_form.html')

        # Test post request (creating a project)
        response = self.client.post(reverse('resume:create-project'), {
            'title': 'New Test Project',
            'description': 'New Test Project Description',
            'technologies': 'Python, Django'
        })
        self.assertRedirects(response, reverse('resume:projects-list'))
        self.assertTrue(Project.objects.filter(title='New Test Project').exists())

    def test_project_list_view(self):
        response = self.client.get(reverse('resume:projects-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/projects_list.html')
        self.assertIn(self.project, response.context['projects'])

    def test_project_update_view(self):
        response = self.client.get(reverse('resume:update-project', kwargs={'pk': self.project.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_update.html')

        # Test post request (updating a project)
        response = self.client.post(reverse('resume:update-project', kwargs={'pk': self.project.pk}), {
            'title': 'Updated Project Title',
            'description': 'Updated Project Description',
            'technologies': 'Updated Technologies'
        })
        self.assertRedirects(response, reverse('resume:projects-list'))
        self.project.refresh_from_db()
        self.assertEqual(self.project.title, 'Updated Project Title')

    def test_project_delete_view(self):
        response = self.client.get(reverse('resume:delete-project', kwargs={'pk': self.project.pk}))
        self.assertEqual(response.status_code, 200)

        # Test delete request
        response = self.client.post(reverse('resume:delete-project', kwargs={'pk': self.project.pk}))
        self.assertRedirects(response, reverse('resume:projects-list'))
        self.assertFalse(Project.objects.filter(pk=self.project.pk).exists())

    def test_education_create_view(self):
        response = self.client.get(reverse('resume:create-education'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resume/education_create_form.html')

        # Test post request (creating education)
        response = self.client.post(reverse('resume:create-education'), {
            'degree': 'New Test Degree',
            'institution': 'New Test University',
            'graduation_year': '2024'
        })
        self.assertRedirects(response, reverse('resume:education-list'))
        self.assertTrue(Education.objects.filter(degree='New Test Degree').exists())

    def test_education_list_view(self):
        response = self.client.get(reverse('resume:education-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resume/education_list.html')
        self.assertIn(self.education, response.context['educations'])

    def test_education_delete_view(self):
        response = self.client.get(reverse('resume:delete-education', kwargs={'pk': self.education.pk}))
        self.assertEqual(response.status_code, 200)

        # Test delete request
        response = self.client.post(reverse('resume:delete-education', kwargs={'pk': self.education.pk}))
        self.assertRedirects(response, reverse('resume:education-list'))
        self.assertFalse(Education.objects.filter(pk=self.education.pk).exists())

