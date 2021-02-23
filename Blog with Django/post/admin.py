from django.contrib import admin
from .models import Subject, Author, Post, Comment, PostViewCount

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display= ('content', 'user',)
    class Meta:
        model=admin
        


admin.site.register(Subject)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(PostViewCount)
admin.site.register(Comment, CommentAdmin)
