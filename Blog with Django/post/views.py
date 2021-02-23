from django.shortcuts import render, redirect
from django.db.models import Count, Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post, Author, PostViewCount
from django.urls import reverse
from marketing.models import Marketing as Signup
from django.shortcuts import get_object_or_404
from .forms import CommentForm, PostForm


def get_category_count():
    queryset = Post.objects.values(
        'categories__title').annotate(Count('categories__title'))
    return queryset


def get_author(request):
    return Author.objects.get(id=request.user.id)


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) or Q(description__icontains=query))
    context = {
        'queryset': queryset
    }
    return render(request, 'blog.html', context)


def home(request):
    posts = Post.objects.all().order_by('-created')[:3]
    latest = Post.objects.all().order_by('-created')[:3]

    if request.method == 'POST':
        email = request.POST['email']
        signup = Signup()
        signup.email = email
        signup.save()

    context = {
        'posts': posts,
        'latest': latest
    }
    return render(request, 'index.html', context)


def blog(request):
    category_count = get_category_count()
    posts = Post.objects.all()
    paginator = Paginator(posts, 4)
    recent_post = Post.objects.order_by('-created')[:3]
    page_reuest_var = 'page'
    page = request.GET.get(page_reuest_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'queryset': paginated_queryset,
        'page_reuest_var': page_reuest_var,
        'recent_post': recent_post,
        'category_count': category_count
    }
    return render(request, 'blog.html', context)


def post(request, id):
    category_count = get_category_count()
    recent_post = Post.objects.order_by('-created')[:3]
    post = get_object_or_404(Post, id=id)
    PostViewCount.objects.get_or_create(user=request.user, post=post)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            form = CommentForm()
    context = {
        'post': post,
        'category_count': category_count,
        'recent_post': recent_post,
        'form': form
    }
    return render(request, 'post.html', context)


def create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_author(request)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.author = author
            form.save()
            return redirect('blog-list')
    context = {
        'form': form
    }
    return render(request, 'post_create.html', context)


def update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('post-detail', kwargs={'id': form.instance.id}))
    context = {
        'form': form,
        'id': post.id
    }
    return render(request, 'post_update.html', context)


def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('blog-list')
