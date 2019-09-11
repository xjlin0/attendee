from django.db import models
from django.urls import reverse

from . import RecordStatusEnum, Utility


class ProgramGroup(models.Model, Utility):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=50, blank=True, null=False, db_index=True)
    info = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=False)
    program_progressions = models.ManyToManyField('ProgramProgression', through='ProgramSession')
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    def get_absolute_url(self):
        return reverse('character_detail', args=[str(self.id)])

    class Meta:
        db_table = 'mainsite_program_groups'

    def __str__(self):
        return '%s %s %s' % (self.name, self.info or '', self.url)
