from django.urls import path
from django.conf.urls import url, include
from django.urls import re_path
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.users),
    # path('users', views.users, name='users'),
]