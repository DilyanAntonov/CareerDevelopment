from django.views.generic import FormView, TemplateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib import messages

from career.users.forms import UserRegistrationForm
from career.users.models import User


class UserRegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:registration-success')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'users/login.html'

    def form_valid(self, form):
        messages.success(self.request, 'You have successfully logged in.')
        return super().form_valid(form)


class RegistrationSuccessView(TemplateView):
    template_name = 'users/registration_success.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'user'
