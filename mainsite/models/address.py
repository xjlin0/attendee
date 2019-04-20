from django.db import models
from .link_note import LinkNote


class Address(models.Model):
    email1 = models.CharField(max_length=100, null=True, db_index=True)
    email2 = models.CharField(max_length=100, null=True)
    phone1 = models.CharField(max_length=15, null=True, db_index=True)
    phone2 = models.CharField(max_length=15, null=True)
    address_type = models.CharField(max_length=20, null=True)
    street1 = models.CharField(max_length=50, null=True)
    street2 = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=10, null=True)
    zip_code = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    class Meta:
        db_table = 'mainsite_address'

    @property
    def notes(self):
        return LinkNote.objects.filter(
            link_table='mainsite_address',
            link_id=self.id
        )

    def __str__(self):
        return '%s %s %s %s %s' % (self.address_type, self.street1, self.city, self.state, self.zip_code)
