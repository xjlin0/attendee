from django.db import models
from django.urls import reverse

from . import RecordStatusEnum, Utility


class ProgramProgression(models.Model, Utility):
    name = models.CharField(max_length=50, blank=True, null=False, db_index=True)
    display_order = models.IntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    def get_absolute_url(self):
        return reverse('program_progression_detail', args=[str(self.id)])

    class Meta:
        db_table = 'mainsite_program_progressions'

    def __str__(self):
        return '%s %s' % (self.name, self.display_order or '')