from django.db import models


class LinkNote(models.Model):
    link_table = models.CharField(max_length=50, db_index=True)
    link_id = models.IntegerField(db_index=True)
    note_type = models.CharField(max_length=20, blank=True, null=True)
    note_text = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default="active", null=False)

    def __str__(self):
        return '%s %s %s' % (self.link_table, self.link_id, self.note_text)
