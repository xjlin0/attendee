from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from . import RecordStatusEnum, Utility, ProgramGroup


class ProgramTeam(models.Model, Utility):
    link_notes = GenericRelation('LinkNote')
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    program_group = models.ForeignKey(ProgramGroup, null=False, blank=False, on_delete=models.SET(0))
    name = models.CharField(max_length=50, blank=True, null=True)
    display_order = models.IntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    class Meta:
        db_table = 'mainsite_program_teams'

    def __str__(self):
        return '%s %s %s %s' % (self.program_session, self.name or '', self.location, self.start_time)

