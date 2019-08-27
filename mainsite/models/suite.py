from django.db import models
from django.urls import reverse

from .building import Building
from .enum import RecordStatusEnum
from .utility import Utility


class Suite(models.Model, Utility):
    name = models.CharField(max_length=50, blank=False, null=False, db_index=True)
    building = models.ForeignKey(Building, null=True, on_delete=models.SET_NULL)
    location = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    def get_absolute_url(self):
        return reverse('suite_detail', args=[str(self.id)])

    def __str__(self):
        return '%s %s %s' % (self.building, self.name, self.location or '')
