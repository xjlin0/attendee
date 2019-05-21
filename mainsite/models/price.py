from django.db import models
from django.utils import timezone

from .event import Event
from .enum import RecordStatusEnum


class Price(models.Model):
    price_label = models.CharField(max_length=50, default=str(timezone.now().year) + " summer retreat")
    event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)
    price_type = models.CharField(max_length=20, db_index=True)
    start_date = models.DateTimeField(default=timezone.now, blank=False, db_index=True)
    price_value = models.DecimalField(max_digits=8, decimal_places=2, default=999999)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    def __str__(self):
        return '%s %s %s %s %s' % (self.event, self.price_label, self.start_date, self.price_type, self.price_value)
