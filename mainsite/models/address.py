from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from . import RecordStatusEnum, Utility


class Address(models.Model, Utility):
    link_notes = GenericRelation('LinkNote')
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    events = models.ManyToManyField('Event', through='EventAddress')
    attendings = models.ManyToManyField('Attending', through='AttendingAddress')
    email1 = models.EmailField(blank=True, null=True, max_length=190, db_index=True)
    email2 = models.EmailField(blank=True, null=True, max_length=190)
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

    def get_absolute_url(self):
        return reverse('address_detail', args=[str(self.id)])

    class Meta:
        db_table = 'mainsite_addresses'

    @property
    def street(self):
        return ('{street1} {street2}').format(street1=self.street1, street2=self.street2 or '').strip()

    def __str__(self):
        return '%s, %s, %s. %s %s' % (self.street, self.city, self.zip_code, self.phone1 or '', self.email1 or '')
