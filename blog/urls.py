from django.urls import path
from . import views
from .views import ContactView, ReservationView, PersonalAreaView


urlpatterns = [
    # главная страница
    path("", views.index, name='index'),
    # о нас
    path("about", views.about, name='about'),
    # меню
    path("menu", views.menu, name='menu'),
    # свяжитесь с нами
    path('contact', ContactView.as_view(), name='contact'),
    # бронь стола
    path('reservation', ReservationView.as_view(), name='reservation'),
    # личный кабинет
    path('profile/', PersonalAreaView.as_view(), name='profile'),

]
