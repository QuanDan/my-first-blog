from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    #/post/42/
    url(r'^post/(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),
    #/post/new/
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<post_id>\d+)/edit/$', views.post_edit, name='post_edit'),
]