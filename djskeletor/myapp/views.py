# -*- coding: utf-8 -*-

"""URLs for all views."""

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from djtools.utils.mail import send_mail

from djskeltor.myapp.forms import MyForm


def home(request, pid=None):
    """Home view."""
    if settings.DEBUG:
        to_list = [settings.SERVER_EMAIL]
    else:
        to_list = [settings.MY_APP_EMAIL]

    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            grad = form.save()
            email = settings.DEFAULT_FROM_EMAIL
            if grad.email:
                email = grad.email
            subject = "[Submit] {0} {1}".format(grad.first_name, grad.last_name)
            send_mail(
                request, to_list, subject, email, 'myapp/email.html', grad,
            )
            return HttpResponseRedirect(reverse_lazy('myapp_success'))
    else:
        form = MyForm()
    return render(request, 'myapp/form.html', {'form': form})


def search(request):
    """Generic search."""
    return render(request, 'myapp/search.html', {})
