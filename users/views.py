from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.models import User
from forum.models import Post

# Create your views here.


def users(request):
    users = User.objects.all()
    
    context = {
        'users': users
        
    }
    return render(request, 'users/users.html', context)
def index(request):
    posts = Post.objects.all()
    stickied = Post.objects.filter(stickied__isnull=False).distinct()
    context = {
        'posts': posts,
        'stickied': stickied,
        
    }
    return render(request, 'users/home.html', context)
