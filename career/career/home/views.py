from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import redirect
from django.utils.translation import activate
from django.conf import settings


class IndexView(TemplateView):
    template_name = 'home/index.html'


class SwitchLanguageView(View):
    def get(self, request, language_code):
        next_url = request.GET.get('next', '/')
        activate(language_code)
        response = redirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language_code)
        return response
