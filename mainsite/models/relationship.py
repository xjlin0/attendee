from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from . import Utility, Attendee, RecordStatusEnum


class Relationship(models.Model, Utility):
    notes = GenericRelation('LinkNote')
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    from_attendee = models.ForeignKey(Attendee, related_name='from_attendee', on_delete=models.SET(0))
    to_attendee = models.ForeignKey(Attendee, related_name='to_attendee', on_delete=models.SET(0))
    relation = models.CharField(max_length=25, null=False, blank=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    class Meta:
        db_table = 'mainsite_relationships'
        constraints = [
            models.UniqueConstraint(fields=['from_attendee', 'to_attendee'], name="from_attendee_to_attendee")
        ]

    def __str__(self):
        return '%s %s %s' % (self.from_attendee, self.to_attendee, self.relation)
