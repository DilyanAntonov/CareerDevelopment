from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, UpdateView, DeleteView, CreateView
from django.utils.translation import gettext_lazy as _

from .forms import CompanyRegistrationForm
from .models import Company
from ..application.models import Application
from ..listings.forms import JobListingForm
from ..listings.models import JobListing
from ..users.forms import CompanyUpdateForm, UserUpdateForm
from ..users.models import User


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CompanyRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_company


class CompanyRegistrationView(FormView):
    form_class = CompanyRegistrationForm
    template_name = 'companies/register.html'
    success_url = reverse_lazy('users:registration-success')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.form_method = 'post'
        form.helper.add_input(Submit('submit', _('Register'), css_class='btn btn-primary'))
        return form

    def form_valid(self, form):
        company = form.save(commit=False)
        company.save()
        return super().form_valid(form)


class CompanyLoginView(LoginView):
    template_name = 'companies/login.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.form_method = 'post'
        form.helper.add_input(Submit('submit', 'Login', css_class='btn btn-primary'))
        return form

    def form_valid(self, form):
        messages.success(self.request, 'You have successfully logged in.')
        return super().form_valid(form)


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'companies/company_detail.html'
    context_object_name = 'company'


class CompanyInfo(DetailView):
    model = Company
    template_name = 'companies/company_info.html'
    context_object_name = 'company'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job_listings'] = JobListing.objects.filter(company=self.object)
        return context


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


class JobListingCreateView(LoginRequiredMixin, CompanyRequiredMixin, CreateView):
    model = JobListing
    form_class = JobListingForm
    template_name = 'companies/job_create.html'

    def get_success_url(self):
        return reverse_lazy('companies:manage-job-listings', kwargs={'pk': self.request.user.id})

    def form_valid(self, form):
        form.instance.company = Company.objects.get(id=self.request.user.id)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.get(id=self.request.user.id)
        return context


class JobListingUpdateView(LoginRequiredMixin, UpdateView):
    model = JobListing
    fields = ['title', 'description', 'requirements', 'location', 'employment_type', 'salary_min', 'salary_max']
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


class JobListingMonitorView(LoginRequiredMixin, CompanyRequiredMixin, DetailView):
    model = JobListing
    template_name = 'companies/job_listing_monitor.html'
    context_object_name = 'job_listing'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job_listing = self.get_object()
        applications = Application.objects.filter(job_listing=job_listing).select_related('user', 'job_listing')

        context['applications'] = applications
        return context
