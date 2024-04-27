from django.urls import path
from .views import JobListingListView, JobListingCreateView, JobListingDetailView

app_name = 'listings'

urlpatterns = [
    path('', JobListingListView.as_view(), name='list'),
    path('create/', JobListingCreateView.as_view(), name='create'),
    path('<int:pk>/', JobListingDetailView.as_view(), name='detail'),
]
