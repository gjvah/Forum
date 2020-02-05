from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('users.urls')),
    path('static/', include('forum.urls')),
    # path('static/', TemplateView.as_view(template_name='base.html'), name='home'),
    path('users/', include('users.urls')),
    path('forum/', include('forum.urls')),
    re_path(r'^tinymce/', include('tinymce.urls')),
    url('avatar/', include('avatar.urls')),
]
