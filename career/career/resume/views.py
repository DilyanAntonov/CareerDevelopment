from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Resume
from .forms import ResumeForm
from django.urls import reverse_lazy


class ResumeCreateView(LoginRequiredMixin, CreateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'resume/resume_create_form.html'
    success_url = reverse_lazy('resume:resume-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ResumesListView(LoginRequiredMixin, ListView):
    model = Resume
    context_object_name = 'resumes'
    template_name = 'resume/resume_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_resumes'] = Resume.objects.count()
        return context
