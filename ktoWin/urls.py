from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^page/(?P<page>[0-9]+)/$', views.index, name='index_page'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post, name='post_by_pk'),
    url(r'^find/(?P<tag>[a-zA-Z0-9_а-яА-Я ]+)$', views.find_by_tag, name='find_by_tag'),
    # url(r'^find/(?P<tag>[a-zA-Z0-9_а-яА-Я ]+)/page/(?P<page>[0-9]+)/$', views.find_by_tag, name='find_by_tag_page'),
    url(r'^new/$', views.new_post, name='new_post'),
    url(r'^hot/$', views.hot, name='hot'),
    # url(r'^hot/page/(?P<page>[0-9]+)/$', views.hot, name='hot_page'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^search/$', views.search, name='search'),
    url(r'^test/$', views.test, name='test'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
