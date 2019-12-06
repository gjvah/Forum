from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.


def users(request):
    users = User.objects.all()
    
    context = {
        'users': users
        
    }
    return render(request, 'users/users.html', context)
