from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from career.companies.models import Company


class CompanyRequiredMixin:
    """
    Verify that the current user is a company.
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_company:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class CompanyContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if hasattr(self.request.user, 'company'):
            context['company'] = self.request.user.company
        return context
