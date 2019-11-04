from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from . import RecordStatusEnum, Utility, ProgramProgression, ProgramGroup


class ProgramSession(models.Model, Utility):
    link_notes = GenericRelation('LinkNote')
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    program_progression = models.ForeignKey(ProgramProgression, blank=False, null=False, on_delete=models.SET(0))
    program_group = models.ForeignKey(ProgramGroup, null=True, on_delete=models.SET_NULL)
    attendings = models.ManyToManyField('Attending', through='ProgramParticipation')
    name = models.CharField(max_length=50, blank=True)
    # link = models.CharField(max_length=254, blank=True)
    start_at = models.DateTimeField(blank=False, null=False)
    end_at = models.DateTimeField(blank=True, null=True)
    site_type = models.ForeignKey(ContentType, on_delete=models.SET(0), help_text='location: django_content_type id for table name')
    site_id = models.BigIntegerField()
    location = GenericForeignKey('site_type', 'site_id')
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    # from itertools import groupby
    # from operator import attrgetter
    #
    # ordered_program_sessions = ProgramSession.objects.order_by('program_group', 'start_at')
    # program_sessions_grouped_by_program_groups = {
    #     k: list(v)
    #     for k, v in groupby(ordered_program_sessions, attrgetter('program_group'))
    # } #=> {<ProgramGroup: The Rock  >: [<ProgramSession: The Rock #1...>, <ProgramSession: The Rock #2...>]}

    def get_absolute_url(self):
        return reverse('program_session_detail', args=[str(self.id)])

    class Meta:
        db_table = 'mainsite_program_sessions'
        ordering = ['program_group', 'program_progression', 'start_at']
        constraints = [
            models.UniqueConstraint(fields=['program_group_id', 'site_type_id', 'site_id', 'start_at'], name='uniq_group_location_time')
        ]

    def __str__(self):
        return '%s %s %s %s' % (self.program_group, self.start_at, self.name or '', self.location or '')
