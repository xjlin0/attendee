from django.db import models
from .link_note import LinkNote
from .enum import RecordStatusEnum

class Address(models.Model):
    email1 = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    email2 = models.CharField(max_length=100, blank=True, null=True)
    phone1 = models.CharField(max_length=15, blank=True, null=True, db_index=True)
    phone2 = models.CharField(max_length=15, blank=True, null=True)
    address_type = models.CharField(max_length=20, null=True)
    street1 = models.CharField(max_length=50, blank=True, null=True)
    street2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=10, default='CA')
    zip_code = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    class Meta:
        db_table = 'mainsite_address'

    @property
    def notes(self):
        return LinkNote.objects.filter(
            status=self.status,
            link_table='mainsite_address',
            link_id=self.id
        )

    def __str__(self):
        return '%s %s %s %s %s' % (self.address_type, self.street1, self.city, self.state, self.zip_code)
