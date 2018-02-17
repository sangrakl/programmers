from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'leave'
urlpatterns = [
    url(r'^leave/$', views.index, name = 'home'),
    url(r'^leave/detail/$', views.detail),
]
