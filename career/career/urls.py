from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('career.users.urls', namespace='users')),
    path('companies/', include('career.companies.urls', namespace='companies')),
    path('listings/', include('career.listings.urls', namespace='listings')),
    path('', include('career.home.urls', namespace='')),
]
