from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostView

app_name = BlogConfig.name

urlpatterns = [
    path('', PostView.as_view(template_name='blog/blog.html'), name='post'),
]
