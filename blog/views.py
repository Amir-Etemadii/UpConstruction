from django.shortcuts import render, get_object_or_404
from .models import *

def blog(request):
    posts = Post.active_objects.all().order_by('-created_at')

    context = {
        'posts':posts
    }

    return render(request, 'blog/blog.html', context)

def blog_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'blog/blog_details.html', {'post':post})