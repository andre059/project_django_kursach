from django.contrib import admin

from blog.models import Post, Comments, Likes


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('heading', 'author', 'blog_body', 'date_publication')
    list_filter = ('author', 'date_publication',)


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post')
    list_filter = ('email', 'name',)


@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('ip', 'pos')
