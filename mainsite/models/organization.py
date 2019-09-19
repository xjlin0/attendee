from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from . import RecordStatusEnum, Utility


class Organization(models.Model, Utility):
    link_notes = GenericRelation('LinkNote')
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    class Meta:
        db_table = 'mainsite_organizations'

    def __str__(self):
        return '%s' % (self.name)

