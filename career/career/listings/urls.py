from django.urls import path
from .views import JobListingListView

app_name = 'listings'

urlpatterns = [
    path('', JobListingListView.as_view(), name='list'),
]
