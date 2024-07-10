from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from .forms import CompanyRegistrationForm
from .models import Company
from ..listings.models import JobListing
from ..users.forms import CompanyUpdateForm, UserUpdateForm
from ..users.models import User


class CompanyRegistrationView(FormView):
    form_class = CompanyRegistrationForm
    template_name = 'companies/register.html'
    success_url = reverse_lazy('users:registration-success')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        return super().form_valid(form)


class CompanyLoginView(LoginView):
    template_name = 'companies/login.html'

    def form_valid(self, form):
        messages.success(self.request, 'You have successfully logged in.')
        return super().form_valid(form)


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'companies/company_detail.html'
    context_object_name = 'company'


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'companies/company_update.html'

    def get_success_url(self):
        return reverse_lazy('companies:company-detail', kwargs={'pk': self.object.pk})

    def get_object(self):
        if self.request.user.is_company:
            return Company.objects.get(pk=self.request.user.pk)
        else:
            return User.objects.get(pk=self.request.user.pk)

    def get_form_class(self):
        if self.request.user.is_company:
            return CompanyUpdateForm
        else:
            return UserUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = self.get_object()
        return context


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'companies/password_change.html'
    success_url = reverse_lazy('companies:password_change_done')
    context_object_name = 'company'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.get(pk=self.request.user.pk)
        return context


class ManageJobListingsView(LoginRequiredMixin, ListView):
    model = JobListing
    template_name = 'companies/manage_job_listings.html'
    context_object_name = 'job_listings'

    def get_queryset(self):
        company = get_object_or_404(Company, pk=self.kwargs['pk'])
        return JobListing.objects.filter(company=company)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = get_object_or_404(Company, pk=self.kwargs['pk'])
        return context


class JobListingUpdateView(LoginRequiredMixin, UpdateView):
    model = JobListing
    fields = ['title', 'description', 'requirements', 'location', 'employment_type', 'application_deadline', 'salary_range']
    template_name = 'companies/edit_job_listing.html'
    context_object_name = 'job_listing'

    def get_success_url(self):
        return reverse_lazy('companies:manage-job-listings', kwargs={'pk': self.object.company.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = self.object.company
        return context


class JobListingDeleteView(LoginRequiredMixin, DeleteView):
    model = JobListing
    template_name = 'companies/delete_job_listing.html'
    context_object_name = 'job_listing'

    def get_success_url(self):
        return reverse_lazy('companies:manage-job-listings', kwargs={'pk': self.object.company.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = self.object.company
        return context