from django.urls import path
from .views import NewsListView, NewsDetailView


urlpatterns = [
    # новости
    path("newslist/", NewsListView.as_view(), name='news'),
    # новость
    path('news/<int:pk>', NewsDetailView.as_view(), name='news-detail'),

]
