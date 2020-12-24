from django.urls import path,re_path
from .views import allBlog, blogDetail, blogListview, blogSearch

urlpatterns = [
    path('allblog/', allBlog.as_view()),
    path('blog/<title>/', blogListview.as_view()),
    path('blogdetail/<pk>', blogDetail),
    path('searchBlog', blogSearch)
]
