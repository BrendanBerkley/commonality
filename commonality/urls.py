from django.conf.urls import patterns, url

from commonality import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^(?P<need_id>\d+)/$', views.detail, name="detail"),
    url(r'^post/$', views.post, name="post"),
    url(r'^post/submit-need/$', views.submit, name="post-submit"),
)