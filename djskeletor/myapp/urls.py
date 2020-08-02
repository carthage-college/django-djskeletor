# -*- coding: utf-8 -*-

"""URLs for all views."""

from django.urls import path
from django.views.generic import TemplateView

from djskeletor.myapp import views


urlpatterns = [
    path(
        '<str:pid>/display/',
        views.myview, name='myapp_display'
    ),
    path(
        'myview/',
        views.myview, name='myapp_display_no_pid'
    ),
    path(
        'success/',
        TemplateView.as_view(
            template_name='myapp/success.html'
        ),
        name='myapp_success',
    ),
]
