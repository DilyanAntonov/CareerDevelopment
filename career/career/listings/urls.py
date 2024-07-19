from django.urls import path
from .views import JobListingListView, JobListingDetailView

app_name = 'listings'

urlpatterns = [
    path('', JobListingListView.as_view(), name='list'),
    path('<int:pk>/', JobListingDetailView.as_view(), name='detail'),
]
