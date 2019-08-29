from django.db import models

from . import Event, Attendee, Utility, RecordStatusEnum


class Registration(models.Model, Utility):
    event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)
    main_attendee = models.ForeignKey(Attendee, null=True, on_delete=models.SET_NULL)
    apply_type = models.CharField(max_length=20, null=True)
    apply_key = models.CharField(max_length=50, null=True)
    donation = models.DecimalField(max_digits=8, decimal_places=2, default=999999)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status = models.CharField(max_length=10, db_index=True, default=RecordStatusEnum.ACTIVE, null=False, choices=RecordStatusEnum.choices())

    @property
    def total(self):
        return sum([attending.price for attending in self.attending_set.all()]) + self.donation

    def __str__(self):
        return '%s %s %s' % (self.apply_type, self.main_attendee, self.total)


    class Meta:
        db_table = 'mainsite_registrations'
        ordering = ['main_attendee__last_name', 'main_attendee__first_name']