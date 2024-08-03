from django.urls import path
from .views import NewsCreateView, CompanyNewsListView, NewsDeleteView, NewsListView, NewsDetailView

app_name = 'news'

urlpatterns = [
    path('create/', NewsCreateView.as_view(), name='news_create'),
    path('company/', CompanyNewsListView.as_view(), name='company_news_list'),
    path('delete/<int:pk>/', NewsDeleteView.as_view(), name='news_delete'),
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
]
