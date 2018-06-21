from django.conf.urls import url

from djskeletor.dashboard import views

urlpatterns = [
    url(
        r'^$',
        views.home, name='home'
    ),
]
