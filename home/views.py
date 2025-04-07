from django.shortcuts import render
from blog.models import Post

def index(request):

    three_post = Post.active_objects.all().order_by('-created_at')[0:3]

    return render(request, 'home/index.html', {'posts': three_post})