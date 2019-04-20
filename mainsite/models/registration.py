from django.db import models
from .event import Event
from .attendee import Attendee


class Registration(models.Model):
    event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)
    main_attendee = models.ForeignKey(Attendee, null=True, on_delete=models.SET_NULL)
    apply_type = models.CharField(max_length=20, null=True)
    apply_key = models.CharField(max_length=50, null=True)
    paid_x100 = models.IntegerField(default=0, null=True)
    total_x100 = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return '%s %s %s' % (self.title, self.main_attendee, self.total_x100)