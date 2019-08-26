from django.db import models
from django.urls import reverse
from .link_note import LinkNote
from .enum import RecordStatusEnum
from .formatter import Formatter


class Character(models.Model, Formatter):
    name = models.CharField(max_length=50, blank=True, null=False, db_index=True)
    info = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    def get_absolute_url(self):
        return reverse('character_detail', args=[str(self.id)])

    class Meta:
        db_table = 'mainsite_character'

    @property
    def notes(self):
        return LinkNote.objects.filter(
            status=self.status,
            link_table='mainsite_character',
            link_id=self.id
        )

    def __str__(self):
        return '%s %s' % (self.name, self.info or '')