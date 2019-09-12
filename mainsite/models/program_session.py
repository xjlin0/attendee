from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from . import RecordStatusEnum, Utility, ProgramProgression, ProgramGroup


class ProgramSession(models.Model, Utility):
    notes = GenericRelation('LinkNote')
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    program_progression = models.ForeignKey(ProgramProgression, blank=False, null=False, on_delete=models.SET(0))
    program_group = models.ForeignKey(ProgramGroup, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, blank=True)
    start_time = models.DateTimeField(blank=False, auto_now_add=True)
    end_time = models.DateTimeField(blank=True, auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.SET(0), help_text='location: django_content_type id for table name')
    object_id = models.BigIntegerField()
    location = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    # TABLE_NAME_TO_CLASS = {
    #     Campus._meta.db_table: Campus,
    #     Property._meta.db_table: Property,
    #     Suite._meta.db_table: Suite,
    #     Room._meta.db_table: Room,
    # }

    def get_absolute_url(self):
        return reverse('program_session_detail', args=[str(self.id)])

    # @property
    # def location(self):
    #     return self.TABLE_NAME_TO_CLASS[self.location_type].objects.get(pk=self.location_id)

    class Meta:
        db_table = 'mainsite_program_sessions'
        constraints = [
            models.UniqueConstraint(fields=['program_group_id', 'location_type', 'location_id', 'start_time'], name='uniq_group_location_time')
        ]

    def __str__(self):
        return '%s %s %s %s' % (self.program_group, self.location or '', self.iso_updated_at, self.name or '')
