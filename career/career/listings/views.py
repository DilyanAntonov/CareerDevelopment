import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views import View
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django_filters import rest_framework as filters
from django import forms

from .models import JobListing
from ..application.models import Application
from ..companies.models import Company
from ..resume.models import Resume
from .constants import OPENAI_PROMPT

from openai import OpenAI
from openai.types.chat import ChatCompletion


class JobListingFilter(filters.FilterSet):
    company = filters.ModelChoiceFilter(queryset=Company.objects.all(), widget=forms.Select)
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    employment_type = filters.ChoiceFilter(choices=JobListing.EMPLOYMENT_TYPE_CHOICES)
    salary_min = filters.NumberFilter(field_name='salary_min', lookup_expr='gte')
    salary_max = filters.NumberFilter(field_name='salary_max', lookup_expr='lte')

    class Meta:
        model = JobListing
        fields = ['company', 'title', 'employment_type', 'salary_min', 'salary_max']


class JobListingListView(ListView):
    template_name = 'listings/job_list.html'
    model = JobListing
    paginate_by = 10
    context_object_name = 'jobs'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-posted_date')
        self.filterset = JobListingFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class JobListingDetailView(LoginRequiredMixin, DetailView):
    model = JobListing
    template_name = 'listings/job_detail.html'
    context_object_name = 'job'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_has_resume = Resume.objects.filter(user=self.request.user).exists()
        user_has_applied = Application.objects.filter(user=self.request.user, job_listing=self.object).exists()

        context['user_has_resume'] = user_has_resume
        context['user_has_applied'] = user_has_applied
        return context

    def post(self, request, *args, **kwargs):
        job = self.get_object()
        user = request.user
        resumes = Resume.objects.filter(user=user)
        if Application.objects.filter(user=user, job_listing=job).exists():
            messages.error(request, "You have already applied for this job.")
            return HttpResponseRedirect(reverse('listings:list'))

        if resumes.exists():
            Application.objects.create(
                user=user,
                job_listing=job,
                resume=resumes.first()
            )
            messages.success(request, "You have successfully applied for the job.")
            return HttpResponseRedirect(reverse('listings:list'))
        else:
            messages.error(request, "You need to upload a resume before applying.")
            return HttpResponseRedirect(reverse('resume:create-resume'))


class JobFitScoreView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            job_id = data.get('job_id')
            user = request.user

            resume = Resume.objects.get(user=user)
            job = JobListing.objects.get(id=job_id)

            resume_data = {
                'summary': resume.summary,
                'education': resume.education,
                'experience': resume.experience,
                'skills': resume.skills,
                'languages': [language.name for language in resume.languages.all()],
                'projects': [[project.title, project.technologies, project.description] for project in resume.projects.all()],
                'interests': resume.interests,
            }

            job_data = {
                'title': job.title,
                'description': job.description,
                'requirements': job.requirements,
                'location': job.location,
                'employment_type': job.get_employment_type_display(),
            }

            client = OpenAI()
            result: ChatCompletion = client.chat.completions.create(
                model="gpt-4o-mini",
                top_p=0.5,
                messages=[
                    {"role": "system", "content": "You are a job matching assistant."},
                    {"role": "user", "content": OPENAI_PROMPT.format(resume=resume_data,
                                                                     job=job_data)}
                ]
            )

            message_content = result.choices[0].message.content.strip()
            print(message_content)
            response_data = json.loads(message_content)
            analysis_text = response_data['text']
            score = response_data['score']

            return JsonResponse({'text': analysis_text, 'score': score})


        except Resume.DoesNotExist:
            return JsonResponse({'error': 'Resume not found'}, status=400)
        except JobListing.DoesNotExist:
            return JsonResponse({'error': 'Job listing not found'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
