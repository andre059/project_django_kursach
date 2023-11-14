from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostView, PostDetail, AddComments, AddLikes, DelLikes

app_name = BlogConfig.name

urlpatterns = [
    path('', PostView.as_view(), name='post'),
    path('<int:pk>/', PostDetail.as_view(), name='blog_detail'),
    path('add_comments/<int:pk>/', AddComments.as_view(), name='add_comments'),
    path('<int:pk>/add_likes/', AddLikes.as_view(), name='add_likes'),
    path('<int:pk>/del_likes/', DelLikes.as_view(), name='del_likes'),
]
