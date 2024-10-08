from django.contrib import admin
from django.urls import path, include
from career.home.views import SwitchLanguageView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('career.users.urls', namespace='users')),
    path('companies/', include('career.companies.urls', namespace='companies')),
    path('listings/', include('career.listings.urls', namespace='listings')),
    path('news/', include('career.news.urls')),
    path('trends/', include('career.trends.urls', namespace='trends')),
    path('resume/', include('career.resume.urls', namespace='resume')),
    path('', include('career.home.urls', namespace='')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('switch_language/<str:language_code>/', SwitchLanguageView.as_view(), name='switch_language'),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
