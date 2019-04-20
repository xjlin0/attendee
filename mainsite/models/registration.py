from django.db import models

from .link_note import LinkNote
from .event import Event
from .attendee import Attendee


class Registration(models.Model):
    event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)
    main_attendee = models.ForeignKey(Attendee, null=True, on_delete=models.SET_NULL)
    apply_type = models.CharField(max_length=20, null=True)
    apply_key = models.CharField(max_length=50, null=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=999999)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    @property
    def notes(self):
        return LinkNote.objects.filter(
            link_table='mainsite_attending',
            link_id=self.id
        )

    def __str__(self):
        return '%s %s %s' % (self.title, self.main_attendee, self.total_x100)