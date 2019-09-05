from django.db import models

from . import RecordStatusEnum, Utility


class Division(models.Model, Utility):
    name = models.CharField(max_length=50, blank=False, null=False)
    key = models.CharField(max_length=50, blank=False, null=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    class Meta:
        db_table = 'mainsite_divisions'

    def __str__(self):
        return '%s %s' % (self.name, self.key)

