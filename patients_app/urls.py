from django.conf.urls import patterns, url

from patients_app import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'(?P<pk>\d+)/edit/$', views.edit, name='edit'),
                       url(r'(?P<pk>\d+)/description/$',views.description, name='description'),
                       )
# r'^blahblah sono i regex
# d = digits, w = words
