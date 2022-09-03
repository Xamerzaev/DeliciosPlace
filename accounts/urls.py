from django.urls import path
from django.contrib.auth import views
from .views import SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),

    path('login/', views.LoginView.as_view(), name='login'),

    path('password-change/', views.PasswordChangeView.as_view(
        template_name='registration/password_change.html'),
        name='password_change'),

    path('password-change/done/', views.PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'),
        name='password_change_done'),

    path('password-reset/', views.PasswordResetView.as_view(
        template_name='registration/password_reset.html'),
        name='password_reset'),

    path('password-reset/done/', views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'),
        name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'),
    ]
