from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'leave'
urlpatterns = [
    url(r'^leave/$', views.index, name = 'home'),
    url(r'^leave/detail/$', views.detail, name = 'detail'),
    url(r'^leave/regist/(?P<pk>\d+)/$', views.regist, name = 'regist'),
    url(r'^late/(?P<pk>\d+)/$', views.late_cal, name = 'late_cal'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name = 'delete'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit, name = 'edit'),
    url(r'^contact/$', views.contact, name = 'contact'),
]
