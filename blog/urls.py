from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostView, PostDetail

app_name = BlogConfig.name

urlpatterns = [
    path('', PostView.as_view(), name='post'),
    path('<int:pk>/', PostDetail.as_view(), name='blog_detail'),
]
