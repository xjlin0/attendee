from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from . import RecordStatusEnum


class LinkNote(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    content_type = models.ForeignKey(ContentType, on_delete=models.SET(0))
    object_id = models.BigIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    note_type = models.CharField(max_length=20, blank=True, null=True)
    note_text = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    def __str__(self):
        return '%s %s %s' % (self.content_type, self.content_object, self.note_text)

    class Meta:
        db_table = 'mainsite_link_notes'
        ordering = ('-updated_at',)

    @property
    def iso_updated_at(self):
        return self.updated_at.isoformat()
