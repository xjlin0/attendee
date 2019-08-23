from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

from .link_note import LinkNote
from .attendee import Attendee
from .address import Address
from .registration import Registration
from .enum import RecordStatusEnum, AttendingDivisionEnum
from .formatter import Formatter


class Attending(models.Model, Formatter):
    registration = models.ForeignKey(Registration, null=True, on_delete=models.SET_NULL)
    attendee = models.ForeignKey(Attendee, null=True, on_delete=models.SET_NULL)
    address = models.ManyToManyField(Address)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=999999)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True)
    attending_type = models.CharField(max_length=20, null=True)
    attending_division = models.CharField(choices=AttendingDivisionEnum.choices(), db_index=True, null=True, default=AttendingDivisionEnum.NONE, max_length=30)
    belief = models.CharField(max_length=20, null=True)
    bed_needs = models.IntegerField(default=1)
    mobility = models.IntegerField(default=1000)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    def clean(self):
        if (self.bed_needs < 1 and self.age is None):
            raise ValidationError("You must specify age for kid")

    def get_absolute_url(self):
        return reverse('attending_detail', args=[str(self.id)])


    class Meta:
        db_table = 'mainsite_attending'

    @property
    def notes(self):
        return LinkNote.objects.filter(
            status=self.status,
            link_table='mainsite_attending',
            link_id=self.id
        )

    @property
    def main_contact(self):
        return self.registration.main_attendee

    def __str__(self):
        return '%s %s %s' % (self.attendee, self.attending_program, self.bed_needs)


    class Meta:
        ordering = ['registration']