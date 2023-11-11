"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('car.urls', namespace='car')),
    path('order/', include('order.urls', namespace='order')),
    path('users/', include('users.urls', namespace='users')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('users/activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('password/reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
