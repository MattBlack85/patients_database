from django.conf.urls import patterns, url
from patients_app import views

urlpatterns = patterns('',
                       url(r'^$',views.index,name = 'index'),
                       url(r'^$',views.edit,name = 'editing_database'),
                       
                       )
