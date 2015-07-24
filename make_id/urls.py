from django.conf.urls import patterns, include, url
from django.contrib import admin
from make_id import views

urlpatterns = patterns('',
    url(r'', views.make_and_record_id),
)
