from django.conf.urls import patterns, url

from NFlixApp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^recs/$', views.recs, name='recommendations'),
    url(r'^receng/$', views.receng, name='receng'),
)
