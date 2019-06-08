from django.db import models
from django.core.exceptions import ValidationError
from .enum import RecordStatusEnum

class Attendee(models.Model):
    chinese_name = models.CharField(max_length=20, db_index=True, null=True, blank=True)
    english_name = models.CharField(max_length=50, db_index=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    def __str__(self):
        return '%s %s' % (self.english_name or '', self.chinese_name or '')

    def clean(self):
        if not (self.english_name or self.chinese_name):
            raise ValidationError("You must specify either english_name or chinese_name")

    class Meta:
        ordering = ['english_name', 'chinese_name']