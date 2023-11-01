from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from users.apps import UsersConfig
from users.views import ProfileView, RegisterView

from .views import PasswordResetView, PasswordResetConfirmView


app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('activate/<uidb64>[0-9A-Za-z]+<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}', views.activate, name='activate'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]