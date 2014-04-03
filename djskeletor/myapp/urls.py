from django.conf.urls.defaults import *
from django.contrib import admin

#django discovery
admin.autodiscover()

urlpatterns = patterns('djskeletor.myapp.views',
    url(
        r'^myview/(?P<pid>\d+)/$',
        'myview', name="myapp_display"
    ),
    url(
        r'^search/$',
        'search', name="myapp_search"
    ),
)
