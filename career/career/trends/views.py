from django.views.generic import TemplateView
from .models import JobTrend


class JobTrendsView(TemplateView):
    template_name = 'trends/job_trends.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve all job trends from the database
        job_trends = JobTrend.objects.all()

        # Initialize dictionaries for data
        job_data = {}
        dates = []

        # Organize data by programming language and date
        for trend in job_trends:
            if trend.programming_language not in job_data:
                job_data[trend.programming_language] = []
            job_data[trend.programming_language].append({
                'date': trend.date,
                'number_of_jobs': trend.number_of_jobs
            })

            # Collect dates if not already in the list
            if trend.date not in dates:
                dates.append(trend.date)

        # Sort dates
        dates.sort()

        # Convert job_data into a format suitable for Chart.js
        formatted_job_data = {}
        for language, data in job_data.items():
            data.sort(key=lambda x: x['date'])  # Sort data by date
            formatted_job_data[language] = [entry['number_of_jobs'] for entry in data]

        context['job_data'] = formatted_job_data
        context['dates'] = [date.strftime("%Y-%m-%d") for date in dates]  # Convert dates to string format

        return context