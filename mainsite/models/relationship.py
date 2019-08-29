from django.db import models

from . import Utility, Attendee, RecordStatusEnum


class Relationship(models.Model, Utility):
    main_attendee = models.ForeignKey(Attendee, null=False, blank=False, on_delete=models.SET(0), related_name="primary")
    other_attendee = models.ForeignKey(Attendee, null=True, blank=False, on_delete=models.SET(0), related_name="relative")
    relation_to_main = models.CharField(max_length=20, null=False, blank=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    class Meta:
        db_table = 'mainsite_relationships'

    def __str__(self):
        return '%s %s %s' % (self.main_attendee, self.other_attendee, self.relation_to_main)
