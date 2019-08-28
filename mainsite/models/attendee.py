from django.db import models
from django.core.exceptions import ValidationError

from .enum import RecordStatusEnum, GenderEnum
from .utility import Utility


class Attendee(models.Model, Utility):
    chinese_first_name = models.CharField(max_length=12, db_index=True, null=True, blank=True)
    chinese_last_name = models.CharField(max_length=8, db_index=True, null=True, blank=True)
    first_name = models.CharField(max_length=25, db_index=True, null=True, blank=True)
    last_name = models.CharField(max_length=25, db_index=True, null=True, blank=True)
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
        if not (self.chinese_last_name or self.last_name):
            raise ValidationError("You must specify either chinese_last_name or last_name")

    class Meta:
        db_table = 'mainsite_attendees'
        ordering = ['last_name', 'chinese_last_name']
