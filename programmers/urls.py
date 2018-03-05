
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('elections.urls')),
    url(r'^', include('leave.urls', namespace='leave')),
    url(r'^', include('social_django.urls', namespace='social')),
]
