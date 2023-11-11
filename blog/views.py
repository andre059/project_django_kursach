from django.shortcuts import render
from django.views.generic.base import View

from blog.models import Post


class PostView(View):
    """Вывод записей"""

    model = Post
    template_name = 'blog/blog.html'

    def get(self, request):
        posts = Post.objects.all
        return render(request, 'blog/blog.html', {'posts': posts})



