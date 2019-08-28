from django.db import models
from django.urls import reverse

from .campus import Campus
from .address import Address
from .enum import RecordStatusEnum
from .utility import Utility


class Property(models.Model, Utility):
    name = models.CharField(max_length=50, blank=False, null=False, db_index=True)
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    campus = models.ForeignKey(Campus, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    class Meta:
        db_table = 'mainsite_property'


    def get_absolute_url(self):
        return reverse('property_detail', args=[str(self.id)])

    def __str__(self):
        return '%s %s %s' % (self.campus, self.name, self.address or '')
