from django.db import models
from . import RecordStatusEnum, Utility


class EventAddress(models.Model, Utility):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    event = models.ForeignKey('Event', on_delete=models.SET(0), null=False, blank=False)
    address = models.ForeignKey('Address', on_delete=models.SET(0), null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    class Meta:
        db_table = 'mainsite_event_addresses'
        constraints = [
            models.UniqueConstraint(fields=['event', 'address'], name="event_address")
        ]

    def __str__(self):
        return '%s %s' % (self.event, self.address or '')
