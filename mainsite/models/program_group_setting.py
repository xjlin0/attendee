from django.db import models
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from recurrence.fields import RecurrenceField
from . import RecordStatusEnum, Utility, ProgramGroup


class ProgramGroupSetting(models.Model, Utility):
    link_notes = GenericRelation('LinkNote')
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    program_group = models.ForeignKey(ProgramGroup, null=False, blank=False, on_delete=models.SET(0))
    start_time = models.TimeField(blank=False, default='10:00')
    recurrences = RecurrenceField()
    duration = models.DurationField(default='01:00:00', blank=False, null=False)
    site_type = models.ForeignKey(ContentType, on_delete=models.SET(0), help_text='location: django_content_type id for table name')
    site_id = models.BigIntegerField()
    location = GenericForeignKey('site_type', 'site_id')
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    class Meta:
        db_table = 'mainsite_program_group_settings'

    def get_recurrences(self):
        return ".".join([rule.to_text() for rule in self.recurrences.rrules])

    def __str__(self):
        return '%s %s %s %s' % (self.program_group, self.start_time, self.recurrences, self.location)

