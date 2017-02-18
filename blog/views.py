from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.htm', {'posts': posts})

def post_detail(request, id):
    # Post.objects.get(pk=id)
    post = get_object_or_404(Post, pk=id)
    return render(request, 'blog/post_detail.htm', {'post': post})

def post_form(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', id=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.htm', {'form': form})

def post_edit(request, id):
    # Post.objects.get(pk=id)
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', id=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.htm', {'form': form, 'edit': 1})
