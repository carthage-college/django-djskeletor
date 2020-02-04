# -*- coding: utf-8 -*-

"""URLs for all views."""

from django.conf.urls import path

from djskeletor.dashboard import views


urlpatterns = [
    path('', views.home, name='home'),
]
