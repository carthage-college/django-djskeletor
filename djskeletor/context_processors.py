# -*- coding: utf-8 -*-


from django.conf import settings


def sitevars(request):
    """Expose some settings to the template level."""
    context = {'manager_group': settings.MANAGER_GROUP}
    return context
