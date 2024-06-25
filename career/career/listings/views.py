from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import JobListing
from .forms import JobListingForm
from ..application.models import Application
from ..resume.models import Resume


class JobListingListView(ListView):
    template_name = 'listings/job_list.html'
    model = JobListing
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-posted_date')

        return queryset


class JobListingCreateView(CreateView):
    model = JobListing
    form_class = JobListingForm
    template_name = 'listings/job_create.html'
    success_url = reverse_lazy('listings:list')

    def form_valid(self, form):
        return super().form_valid(form)


class JobListingDetailView(LoginRequiredMixin, DetailView):
    model = JobListing
    template_name = 'listings/job_detail.html'
    context_objectname = 'job'

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
