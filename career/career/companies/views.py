from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from .forms import CompanyRegistrationForm
from .models import Company


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
