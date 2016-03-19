from django.contrib import admin
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

#django discovery
admin.autodiscover()

urlpatterns = patterns('djskeletor.myapp.views',
    url(
        r'^myview/(?P<pid>\d+)/$',
        'myview', name="myapp_display"
    ),
    url(
        r'^myview/$',
        'myview', name="myapp_display_no_pid"
    ),
    url(
        r'^search/$',
        'search', name="myapp_search"
    ),
    url(
        r'^myview/success/$',
        TemplateView.as_view(
            template_name='myapp/success.html'
        ),
        name='myapp_success'
    ),
)
