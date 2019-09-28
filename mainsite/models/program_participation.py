from django.db import models
from django.utils.functional import cached_property
from django.contrib.contenttypes.fields import GenericRelation
from . import RecordStatusEnum, Utility, Attending, Character, ProgramSession, ProgramTeam


class ProgramParticipation(models.Model, Utility):
    link_notes = GenericRelation('LinkNote')
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    program_session = models.ForeignKey(ProgramSession, null=False, blank=False, on_delete=models.SET(0))
    program_team = models.ForeignKey(ProgramTeam, default=None, null=True, blank=True, on_delete=models.SET_NULL, help_text="empty for main group")
    attending = models.ForeignKey(Attending, null=False, blank=False, on_delete=models.SET(0))
    character = models.ForeignKey(Character, null=False, blank=False, on_delete=models.SET(0))
    free = models.IntegerField(default=0, blank=True, null=True, help_text="multitasking: the person cannot join other sessions if negative")
    attend_at = models.DateTimeField(default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    @cached_property
    def brief_program_session(self):
        program_session = self.program_session
        return program_session.program_group.name + program_session.start_at.strftime(" @ %b.%d'%y")

    class Meta:
        db_table = 'mainsite_program_participations'

    def __str__(self):
        return '%s %s %s' % (self.program_session, self.character, self.program_team or '')

