from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from . import RecordStatusEnum, Utility


class Division(models.Model, Utility):
    link_notes = GenericRelation('LinkNote')
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    organization = models.ForeignKey('Organization', null=False, blank=False, on_delete=models.SET(0))
    name = models.CharField(max_length=50, blank=False, null=False)
    key = models.CharField(max_length=50, blank=False, null=False, db_index=True)
    attendings = models.ManyToManyField('Attending', through='AttendingDivision')
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    class Meta:
        db_table = 'mainsite_divisions'

    def __str__(self):
        return '%s %s' % (self.name, self.key)

