from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^page/(?P<page>[0-9]+)/$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post, name='post_by_pk'),
    url(r'^find/(?P<tag>[a-zA-Z0-9]+)$', views.find_by_tag, name='find_by_tag'),
    url(r'^find/(?P<tag>[a-zA-Z0-9]+)/page/(?P<page>[0-9]+)/$', views.find_by_tag, name='find_by_tag'),
    url(r'^new/$', views.new_post, name='new_post'),
    url(r'^hot/$', views.hot, name='hot'),
    url(r'^hot/page/(?P<page>[0-9]+)/$', views.hot, name='hot'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^search/$', views.search, name='search'),
    url(r'^test/$', views.test, name='test'),
]
