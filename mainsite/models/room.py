from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from . import Suite, RecordStatusEnum, Utility


class Room(models.Model, Utility):
    link_notes = GenericRelation('LinkNote')
    program_session = GenericRelation('ProgramSession')
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=50, blank=False, null=False, db_index=True)
    suite = models.ForeignKey(Suite, null=True, on_delete=models.SET_NULL)
    label = models.CharField(max_length=20, blank=True)
    accessibility = models.IntegerField(default=0, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    class Meta:
        db_table = 'mainsite_rooms'


    def get_absolute_url(self):
        return reverse('room_detail', args=[str(self.id)])

    def __str__(self):
        return '%s %s %s' % (self.suite.name, self.name, self.label or '')
