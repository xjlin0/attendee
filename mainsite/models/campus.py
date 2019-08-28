from django.db import models
from django.urls import reverse

from .address import Address
from .enum import RecordStatusEnum
from .utility import Utility


class Campus(models.Model, Utility):
    name = models.CharField(max_length=50, blank=False, null=False, db_index=True)
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    class Meta:
        db_table = 'mainsite_campus'


    def get_absolute_url(self):
        return reverse('campus_detail', args=[str(self.id)])

    def __str__(self):
        return '%s %s' % (self.name, self.address or '')