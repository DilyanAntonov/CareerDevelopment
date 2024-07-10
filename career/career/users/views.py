from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, TemplateView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib import messages

from career.companies.models import Company
from career.users.forms import UserRegistrationForm, UserUpdateForm, CompanyUpdateForm
from career.users.models import User, BaseUser


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


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'users/user_update.html'

    def get_success_url(self):
        return reverse_lazy('users:user-detail', kwargs={'pk': self.object.user.pk})

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


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('users:password_change_done')