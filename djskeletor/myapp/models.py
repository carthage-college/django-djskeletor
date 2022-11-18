# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class MyModel(models.Model):
    """
    Model: ...
    """
    created_by = models.ForeignKey(
        User,
        verbose_name="Created by",
        related_name="mymodel_created_by",
        editable=False,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    updated_by = models.ForeignKey(
        User,
        verbose_name="Updated by",
        related_name="mymodel_updated_by",
        editable=False,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    created_at = models.DateTimeField(
        "Date Created",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        "Date Updated",
        auto_now=True,
    )

    class Meta:
        ordering  = ['-created_at']
        get_latest_by = 'created_at'

    def __str__(self):
        """Default data for display."""
        return self.created_by.username

    def get_absolute_url(self):
        """Default earl."""
        return ('myapp_detail', [str(self.id)])
