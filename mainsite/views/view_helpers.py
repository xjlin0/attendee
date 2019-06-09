class NoteHelper:

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['note_counts'] = len(self.object.notes)
        data['note_class'] = '' if data['note_counts'] > 0 else 'd-none'
        return data
