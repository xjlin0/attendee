from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from . import Utility, Event, RecordStatusEnum


class Price(models.Model, Utility):
    notes = GenericRelation('LinkNote')
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    price_label = models.CharField(max_length=50)
    event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)
    price_type = models.CharField(max_length=20, db_index=True)
    start_date = models.DateTimeField(auto_now_add=True, blank=False, db_index=True)
    price_value = models.DecimalField(max_digits=8, decimal_places=2, default=999999)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    class Meta:
        db_table = 'mainsite_prices'

    def __str__(self):
        return '%s %s %s %s %s' % (self.event, self.price_label, self.start_date, self.price_type, self.price_value)
