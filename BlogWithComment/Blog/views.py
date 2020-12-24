from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User

from Blog.models import Blog, Comment, Subject
from .forms import Message_form


# Create your views here.


class allBlog(ListView):
    template_name = 'blogs.html'
    queryset = Blog.objects.all().order_by('-create_at')
    paginate_by = 8


class blogListview(ListView):
    template_name = 'blogs.html'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        category_title = self.kwargs['title']
        context['subject'] = category_title
        return context

    def get_queryset(self, *args, **kwargs):
        subject_title = self.kwargs['title']
        subject_title = subject_title.replace('-', ' ')
        qs = Blog.objects.filter(subject__title=subject_title)
        if qs is None:
            raise Http404('صفحه مورد نظر یافت نشد')
        return Blog.objects.filter(subject__title=subject_title)


def blogDetail(request, *args, **kwargs):
    blog_id = kwargs['pk']
    blog = Blog.objects.get(id=blog_id)
    subject = Subject.objects.get(id=blog.subject_id)
    comment = Comment.objects.filter(blog=blog_id)

    form = Message_form(request.POST or None)
    if form.is_valid():
        title = form.cleaned_data.get('title')
        message = form.cleaned_data.get('message')
        blog.comment_set.create(user=request.user.username, blog=blog_id, title=title, message=message)

    blog = Blog.objects.get(id=blog_id)
    blog.seen += 1
    blog.save()

    context = {
        'blog': blog,
        'comments': comment,
        'form': form,
        'subject': subject
    }
    return render(request, 'blogdetail.html', context)


def blogSearch(request):
    context = {}
    qs = request.GET.get('q')
    blog = Blog.objects.filter(
        Q(title__icontains=qs) |
        Q(description__icontains=qs)
    )
    context['blog'] = blog

    return render(request, 'blogSearch.html', context)
