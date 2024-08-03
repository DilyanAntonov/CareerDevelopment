from django.views.generic import ListView, DetailView

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import News
from .forms import NewsForm
from .mixins import CompanyRequiredMixin, CompanyContextMixin


class NewsCreateView(LoginRequiredMixin, CompanyRequiredMixin, CompanyContextMixin, CreateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_form.html'
    success_url = reverse_lazy('news:company_news_list')

    def form_valid(self, form):
        form.instance.company = self.request.user.company
        return super().form_valid(form)


class CompanyNewsListView(LoginRequiredMixin, CompanyRequiredMixin, CompanyContextMixin, ListView):
    model = News
    template_name = 'news/company_news_list.html'
    context_object_name = 'news_articles'

    def get_queryset(self):
        return News.objects.filter(company=self.request.user.company)


class NewsDeleteView(LoginRequiredMixin, CompanyRequiredMixin, CompanyContextMixin, DeleteView):
    model = News
    template_name = 'news/news_confirm_delete.html'
    success_url = reverse_lazy('news:company_news_list')

    def get_queryset(self):
        return News.objects.filter(company=self.request.user.company)


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_articles'

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_order = self.request.GET.get('sort', 'newest')
        if sort_order == 'oldest':
            queryset = queryset.order_by('date_posted')
        else:
            queryset = queryset.order_by('-date_posted')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort_order'] = self.request.GET.get('sort', 'newest')
        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news_article'
