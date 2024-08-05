from django.urls import path
from .views import JobListingListView, JobListingDetailView, JobFitScoreView

app_name = 'listings'

urlpatterns = [
    path('', JobListingListView.as_view(), name='list'),
    path('<int:pk>/', JobListingDetailView.as_view(), name='detail'),
    path('job-fit-score/', JobFitScoreView.as_view(), name='job-fit-score'),
]
