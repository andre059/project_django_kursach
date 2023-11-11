from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('heading', 'author', 'blog_body', 'date_publication')
    list_filter = ('author', 'date_publication',)
