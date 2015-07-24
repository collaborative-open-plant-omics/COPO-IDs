from django.conf.urls import patterns, include, url
from django.contrib import admin
from make_id import urls

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^id/', include(urls)),
                       )
