from django.views import generic
from django.shortcuts import render, get_object_or_404

from .models import News


class NewsListView(generic.ListView):
    model = News
    paginate_by = 10
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        return context


class NewsDetailView(generic.DetailView):
    model = News

    def news_detail_view(request, primary_key):
        news = get_object_or_404(News, pk=primary_key)
        return render(request,
                      'news/news-detail.html', context={'news': news})
