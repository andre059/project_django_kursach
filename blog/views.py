from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import View
from blog.forms import CommentsForm

from blog.models import Post, Comments, Likes


class PostView(View):
    """Вывод записей"""

    model = Post

    def get(self, request):
        posts = Post.objects.all
        return render(request, 'blog/blog.html', {'post_list': posts})


class PostDetail(View):
    """Отдельная страница записи"""
    model = Post

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        return render(request, 'blog/blog_detail.html', {'post': post})


class AddComments(View):
    """Добавление коментариев"""
    model = Comments

    def post(self, request, pk):
        form = CommentsForm(request.POST)

        # проверка на валидацию
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()

        return redirect(reverse('blog:blog_detail', args=[self.kwargs.get('pk')]))


def get_client_ip(request):
    """получение IP-адреса клиента"""
    x_forwarded_for = request.META.get('HTTP_XFORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # берём первый элемент из списка
    else:
        ip = request.META.get('REMOTE_ADDR')  # IP-адрес системы которая связалась с нашим сайтом
    return ip


class AddLikes(View):
    """Лайк"""

    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)  # получение из БД IP-клиента и id-записи
            return redirect(reverse('blog:blog_detail', args=[self.kwargs.get('pk')]))
        except:
            nev_like = Likes()
            nev_like.ip = ip_client
            nev_like.pos_id = int(pk)
            nev_like.save()
            return redirect(reverse('blog:blog_detail', args=[self.kwargs.get('pk')]))


class DelLikes(View):
    """Дизлайк"""

    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            lik = Likes.objects.get(ip=ip_client)
            lik.delete()
            return redirect(reverse('blog:blog_detail', args=[self.kwargs.get('pk')]))
        except:
            return redirect(reverse('blog:blog_detail', args=[self.kwargs.get('pk')]))



