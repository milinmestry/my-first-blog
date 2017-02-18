from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_form, name='post_form'),
    url(r'^post/(?P<id>\d+)/edit/$', views.post_edit, name='post_edit'),    
]
