from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from . import RecordStatusEnum, Utility


class Character(models.Model, Utility):
    notes = GenericRelation('LinkNote')
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=50, blank=True, null=False, db_index=True)
    info = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=50, null=False, default='normal', db_index=True)
    display_order = models.IntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    def get_absolute_url(self):
        return reverse('character_detail', args=[str(self.id)])

    class Meta:
        db_table = 'mainsite_characters'

    def __str__(self):
        return '%s %s %s' % (self.name, self.type, self.info or '')
