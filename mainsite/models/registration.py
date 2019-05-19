from django.db import models

from .link_note import LinkNote
from .event import Event
from .attendee import Attendee


class Registration(models.Model):
    event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)
    main_attendee = models.ForeignKey(Attendee, null=True, on_delete=models.SET_NULL)
    apply_type = models.CharField(max_length=20, null=True)
    apply_key = models.CharField(max_length=50, null=True)
    donation = models.DecimalField(max_digits=8, decimal_places=2, default=999999)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    archived = models.NullBooleanField(default=False, null=True, db_index=True, help_text="NULL means deleted")

    @property
    def notes(self):
        return LinkNote.objects.filter(
            archived=self.archived,
            link_table='mainsite_registration',
            link_id=self.id
        )

    @property
    def total(self):
        return sum([attending.price for attending in self.attending_set.all()]) + self.donation

    def __str__(self):
        return '%s %s %s' % (self.apply_type, self.main_attendee, self.total)


    class Meta:
        ordering = ['main_attendee__english_name', 'main_attendee__chinese_name']