from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
from Blog.models import Blog, Comment
from .forms import Message_form


# Create your views here.


class allBlog(ListView):
    template_name = 'blogs.html'
    queryset = Blog.objects.all()
    paginate_by = 6


class blogListview(ListView):
    template_name = 'blogs.html'
    paginate_by = 3

    def get_queryset(self, *args, **kwargs):
        subject_title = self.kwargs['title']
        subject_title = subject_title.replace('-', ' ')
        qs = Blog.objects.filter(subject__title=subject_title)
        if qs is None:
            raise Http404('صفحه مورد نظر یافت نشد')
        return Blog.objects.filter(subject__title=subject_title)


def blogDetail(request, *args, **kwargs):
    blog_id = kwargs['bookid']
    blog = Blog.objects.get(id=blog_id)
    comment = Comment.objects.filter(blog=blog_id)

    form = Message_form(request.POST or None)
    if form.is_valid():
        title = form.cleaned_data.get('title')
        message = form.cleaned_data.get('message')
        Message_form.create(user=request.user.id, blog=blog_id, title=title, message=message)

    seen = Blog.objects.get(id=blog_id)
    seen += 1
    seen.save()

    context = {
        'blog': blog,
        'comment': comment,
        'form': form
    }
    return render(request, 'blogdetail.html', context)
