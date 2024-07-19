from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django_filters import rest_framework as filters
from django import forms

from .models import JobListing
from ..application.models import Application
from ..companies.models import Company
from ..resume.models import Resume


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
