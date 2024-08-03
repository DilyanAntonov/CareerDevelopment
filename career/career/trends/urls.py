from django.urls import path
from career.trends.views import JobTrendsView

app_name = 'trends'

urlpatterns = [
    path('job-trends/', JobTrendsView.as_view(), name='job-trends'),
]
