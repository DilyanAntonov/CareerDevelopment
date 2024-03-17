from django.views.generic import ListView
from .models import JobListing
# from .forms import JobSearchForm  # Uncomment and define this form for search functionality.


class JobListingListView(ListView):
    template_name = 'listings/job_list.html'
    model = JobListing
    paginate_by = 10
    # form_class = JobSearchForm  # Define and use this form for filtering if needed.

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-posted_date')  # Assuming you have a date_posted field.

        # Example search form usage, adapt based on your actual form and model fields.
        # if self.form_class:
        #     search_form = self.form_class(self.request.GET)
        #     if search_form.is_valid():
        #         keyword = search_form.cleaned_data['keyword']
        #         if keyword:
        #             queryset = queryset.filter(description__icontains=keyword)
        #         # Add more filters based on your form fields and model attributes.

        return queryset
