from django.db import models

from .link_note import LinkNote
from .attendee import Attendee
from .address import Address
from .registration import Registration

class Attending(models.Model):
    registration = models.ForeignKey(Registration, null=True, on_delete=models.SET_NULL)
    attendee = models.ForeignKey(Attendee, null=True, on_delete=models.SET_NULL)
    address = models.ManyToManyField(Address)
    price_x100 = models.IntegerField(default=100, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, null=True)
    attending_type = models.CharField(max_length=20, null=True)
    attending_program = models.CharField(max_length=30, null=True, db_index=True)
    belief = models.CharField(max_length=20, null=True)
    bed_needs = models.IntegerField(default=1)
    mobility = models.IntegerField(default=1000)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    class Meta:
        db_table = 'mainsite_attending'

    @property
    def notes(self):
        return LinkNote.objects.filter(
            link_table='mainsite_attending',
            link_id=self.id
        )

    def __str__(self):
        return '%s %s %s' % (self.attendee, self.attending_program, self.bed_needs)
