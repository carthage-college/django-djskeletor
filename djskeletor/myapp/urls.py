from django.conf.urls.defaults import *
from django.contrib import admin

#django discovery
admin.autodiscover()

urlpatterns = patterns('myapp.views',
    url(r'^myapp/display/(?P<pid>\d+)/$','display', name="myapp_display"),
    url(r'^myapp/search/$','search', name="myapp_search"),
    url(r'^myapp/admin/(.*)', admin.site.root),
)
