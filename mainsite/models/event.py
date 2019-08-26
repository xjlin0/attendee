from django.db import models
from django.urls import reverse

import datetime

from .address import Address
from .enum import RecordStatusEnum
from .utility import Utility


class Event(models.Model, Utility):
    name = models.CharField(max_length=50, db_index=True, default=str(datetime.date.today().year) + " summer retreat")
    address = models.ManyToManyField(Address)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])

    def __str__(self):
        return '%s' % self.name

    def get_addresses(self):
        return "\n".join([a.street1 + a.city for a in self.address.all()])
