from django.conf.urls import url
from . import views
from django.urls import re_path

urlpatterns = [

    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^new_post$', views.new_post),
    url(r'^edit$', views.edit),
    url(r'^details$', views.details),
    url(r'^delete/(?P<number>\d+)$', views.delete),
    url(r'^details/(?P<number>\d+)$', views.details),
    url(r'^edit/(?P<number>\d+)$', views.edit),
    url(r'^update/(?P<number>\d+)$', views.update),
    url(r'^add_comment/(?P<number>\d+)$', views.addComment),
    url(r'^add_profile_comment/(?P<number>\d+)/(?P<id>\d+)$', views.addProfileComment),
    url(r'^delete_profile_comment/(?P<number>\d+)/(?P<id>\d+)$', views.deleteProfileComment),
    url(r'^comment_delete/(?P<number>\d+)$', views.comment_delete),
    url(r'^join_trip/(?P<id>\d+)$', views.joinPost),
    url(r'^remove_trip/(?P<id>\d+)$', views.removePost),
    url(r'^like/(?P<id>\d+)$', views.like),
    url(r'^unlike/(?P<id>\d+)$', views.unlike),
    url(r'^stickied/(?P<id>\d+)$', views.stickied),
    url(r'^unstickied/(?P<id>\d+)$', views.unstickied),
    url(r'^user/(?P<id>\d+)$', views.profile),
]