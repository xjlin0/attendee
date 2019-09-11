from django.db import models
from django.urls import reverse

from . import RecordStatusEnum, Utility, Division


class Event(models.Model, Utility):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    addresses = models.ManyToManyField('Address', through='EventAddress')
    name = models.CharField(max_length=50, db_index=True)
    division = models.ForeignKey(Division, null=False, blank=False, on_delete=models.SET(0))
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])

    class Meta:
        db_table = 'mainsite_events'
        ordering = ('-updated_at',)

    def __str__(self):
        return '%s' % self.name

    def get_addresses(self):
        return "\n".join([a.street1 + a.city for a in self.addresses.all()])

    def ttttt(self):
        return "ttttt"

from rest_framework import serializers
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'division', 'ttttt']

# from mainsite.models.event import EventSerializer
# k2=Event.objects.get(pk=2)
# serializer=EventSerializer(k2)
# serializer.data
# #=> {'id': 2, 'name': '2019 Fall kid programs', 'division': 'none', 'ttttt': 'ttttt'}
