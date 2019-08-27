from django.db import models
from django.urls import reverse

from .enum import RecordStatusEnum
from .utility import Utility
from .campus import Campus
from .building import Building
from .suite import Suite
from .room import Room
from .kid_program_progression import KidProgramProgression
from .kid_program_group import KidProgramGroup


class KidProgramLesson(models.Model, Utility):
    kid_program_progression = models.ForeignKey(KidProgramProgression, blank=False, null=False, on_delete=models.SET(0))
    kid_program_group = models.ForeignKey(KidProgramGroup, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, blank=True)
    start_time = models.DateTimeField(blank=False, auto_now_add=True)
    end_time = models.DateTimeField(blank=True, auto_now_add=True)
    location_type = models.CharField(max_length=50)
    location_id = models.IntegerField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    def get_absolute_url(self):
        return reverse('kid_program_lesson_detail', args=[str(self.id)])

    def location(self):
        return ''

    class Meta:
        db_table = 'mainsite_kid_program_group'
        constraints = [
            models.UniqueConstraint(fields=['kid_program_group_id', 'location_type', 'location_id', 'start_time'], name='uniq_group_location_time')
        ]

    def __str__(self):
        return '%s %s %s %s' % (self.kid_program_group, self.location or '', self.iso_updated_at, self.name or '')
