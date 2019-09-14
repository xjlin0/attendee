from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.fields import GenericRelation
from . import RecordStatusEnum, GenderEnum, Utility


class Attendee(models.Model, Utility):
    link_notes = GenericRelation('LinkNote')
    relatives = models.ManyToManyField('self', through='Relationship', symmetrical=False, related_name='related_to+')
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    first_name = models.CharField(max_length=25, db_index=True, null=True, blank=True)
    last_name = models.CharField(max_length=25, db_index=True, null=True, blank=True)
    first_name2 = models.CharField(max_length=12, db_index=True, null=True, blank=True)
    last_name2 = models.CharField(max_length=8, db_index=True, null=True, blank=True)
    other_name = models.CharField(max_length=20, db_index=True, null=True, blank=True)
    gender = models.CharField(max_length=11, blank=False, null=False, default=GenderEnum.UNSPECIFIED, choices=GenderEnum.choices())
    actual_birthday = models.DateTimeField(blank=True, null=True)
    estimated_birthday = models.DateTimeField(blank=True, null=True)
    medical_concern = models.CharField(max_length=50, null=False, blank=False, default="Food allergy: nothing")
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    def __str__(self):
        return '%s %s' % (self.first_name or '', self.last_name or '')

    def clean(self):
        if not (self.last_name or self.last_name2):
            raise ValidationError("You must specify a last_name")

    class Meta:
        db_table = 'mainsite_attendees'
        ordering = ['last_name', 'first_name']
