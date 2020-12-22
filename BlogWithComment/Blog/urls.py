from django.urls import path
from .views import allBlog, blogDetail


urlpatterns = [
    path('allblog', allBlog.as_view()),
    path('blog/<title>', allBlog.as_view()),
    path('blogdetail/<pk>', blogDetail)
]
