from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

from .models import JobListing
from .forms import JobListingForm


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


class JobListingDetailView(DetailView):
    model = JobListing
    template_name = 'listings/job_detail.html'  # Create this template
    context_object_name = 'job'
