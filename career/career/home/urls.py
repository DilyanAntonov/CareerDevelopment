from django.urls import path
from career.home.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
