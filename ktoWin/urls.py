from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^post/$', views.post),
    url(r'^new/$', views.new_post),
    url(r'^settings/$', views.settings),
    url(r'^signup/$', views.signup),
    url(r'^find/$', views.find),
    url(r'^test/$', views.test),
]
