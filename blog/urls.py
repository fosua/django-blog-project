from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'blog.views.home'),
    url(r'^posts/$', 'blog.views.post_list'),
    url(r'^posts/(?P<ID>\d+)/((?P<showComments>.*)/)?$', 'blog.views.post_detail'),
    ## add your url here
    url(r'^posts/search/(?P<anything>.+)/$', 'blog.views.post_search'),
    url(r'^comments/(?P<comm_id>\d+)/edit','blog.views.edit_comment'),
)
