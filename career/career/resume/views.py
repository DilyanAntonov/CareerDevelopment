from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Resume, Project, Education
from .forms import ResumeForm, ProjectForm, EducationForm
from django.urls import reverse_lazy


class ResumeCreateView(LoginRequiredMixin, CreateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'resume/resume_create_form.html'
    success_url = reverse_lazy('resume:resume-detail')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

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


class ResumeUpdateView(LoginRequiredMixin, UpdateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'resume/resume_update.html'
    success_url = reverse_lazy('resume:resume-detail')

    def get_object(self, queryset=None):
        try:
            return self.request.user.resume
        except Resume.DoesNotExist:
            return None

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_create_form.html'
    success_url = reverse_lazy('resume:projects-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_update.html'
    success_url = reverse_lazy('resume:projects-list')

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/projects_list.html'

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('resume:projects-list')

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class EducationCreateView(LoginRequiredMixin, CreateView):
    model = Education
    form_class = EducationForm
    template_name = 'resume/education_create_form.html'
    success_url = reverse_lazy('resume:education-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EducationListView(LoginRequiredMixin, ListView):
    model = Education
    context_object_name = 'educations'
    template_name = 'resume/education_list.html'

    def get_queryset(self):
        return Education.objects.filter(user=self.request.user)


class EducationDeleteView(LoginRequiredMixin, DeleteView):
    model = Education
    success_url = reverse_lazy('resume:education-list')

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)