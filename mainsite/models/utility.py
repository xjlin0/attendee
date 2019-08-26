from .link_note import LinkNote


class Utility:

    @property
    def iso_updated_at(self):
        return self.updated_at.isoformat()

    @property
    def notes(self):
        return LinkNote.objects.filter(
            status=self.status,
            link_table=self._meta.db_table,
            link_id=self.id
        )