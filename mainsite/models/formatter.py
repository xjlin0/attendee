class Formatter:

    @property
    def iso_updated_at(self):
        return self.updated_at.isoformat()
