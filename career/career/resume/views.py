from django.views.generic import CreateView, ListView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Resume, Project
from .forms import ResumeForm, ProjectForm
from django.urls import reverse_lazy


class ResumeCreateView(LoginRequiredMixin, CreateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'resume/resume_create_form.html'
    success_url = reverse_lazy('resume:resume-detail')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ResumeDetailView(LoginRequiredMixin, DetailView):
    model = Resume
    template_name = 'resume/resume_detail.html'

    def get_object(self, queryset=None):
        try:
            return self.request.user.resume
        except Resume.DoesNotExist:
            return None


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_create_form.html'
    success_url = reverse_lazy('resume:projects-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/projects_list.html'


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('resume:projects-list')

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
