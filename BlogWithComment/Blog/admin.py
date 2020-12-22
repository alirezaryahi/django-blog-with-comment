from django.contrib import admin
from Blog.models import Blog, Subject, Comment


# Register your models here.


class blog_admin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'create_at', 'seen']
    search_fields = ['title', 'subject']
    list_filter = ['subject']

    class Meta:
        model = Blog


class comment_admin(admin.ModelAdmin):
    list_display = ['user', 'title', 'message']
    search_fields = ['user']

    class Meta:
        model = Comment


admin.site.register(Blog, blog_admin)
admin.site.register(Comment, comment_admin)
admin.site.register(Subject)
