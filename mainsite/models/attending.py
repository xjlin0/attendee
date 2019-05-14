from django.db import models

from .link_note import LinkNote
from .attendee import Attendee
from .address import Address
from .registration import Registration

class Attending(models.Model):
    registration = models.ForeignKey(Registration, null=True, on_delete=models.SET_NULL)
    attendee = models.ForeignKey(Attendee, null=True, on_delete=models.SET_NULL)
    address = models.ManyToManyField(Address)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=999999)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True)
    attending_type = models.CharField(max_length=20, null=True)
    attending_program = models.CharField(max_length=30, null=True, db_index=True)
    belief = models.CharField(max_length=20, null=True)
    bed_needs = models.IntegerField(default=1)
    mobility = models.IntegerField(default=1000)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
# TODO: add deleted_at for all models and ListView can exclude deleted_at condition

    class Meta:
        db_table = 'mainsite_attending'

    @property
    def notes(self):
        return LinkNote.objects.filter(
            link_table='mainsite_attending',
            link_id=self.id
        )

    @property
    def main_contact(self):
        return self.registration.main_attendee

    def __str__(self):
        return '%s %s %s' % (self.attendee, self.attending_program, self.bed_needs)

