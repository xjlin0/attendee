from django.db import models

# Create your models here.


class Attendee(models.Model):
    chinese_name = models.CharField(max_length=20, db_index=True)
    english_name = models.CharField(max_length=40, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return '%s %s' % (self.english_name, self.chinese_name)
