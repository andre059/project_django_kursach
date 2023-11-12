from django.shortcuts import render
from django.views.generic.base import View

from blog.models import Post


class PostView(View):
    """Вывод записей"""

    model = Post
    # template_name = 'blog/blog.html'

    def get(self, request):
        posts = Post.objects.all
        return render(request, 'blog/blog.html', {'post_list': posts})


class PostDetail(View):
    """Отдельная страница записи"""
    model = Post

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        return render(request, 'blog/blog_detail.html', {'post': post})
