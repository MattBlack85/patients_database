from django.conf.urls import patterns, url

from patients_app import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'(?P<name>\w+)/edit/$', views.edit, name='edit'),
                       )
# r'^blahblah sono i regex
# d = digits, w = words
