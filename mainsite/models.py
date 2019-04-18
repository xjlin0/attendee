from django.db import models
import datetime


# Create your models here.

class LinkNote(models.Model):
    link_table = models.CharField(max_length=50, db_index=True)
    link_id = models.IntegerField(db_index=True)
    note_type = models.CharField(max_length=20)
    note_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return '%s %s %s' % (self.link_table, self.link_id, self.note_text)


class Attendee(models.Model):
    chinese_name = models.CharField(max_length=20, db_index=True)
    english_name = models.CharField(max_length=40, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return '%s %s' % (self.english_name, self.chinese_name)


class Address(models.Model):
    email1 = models.CharField(max_length=100, null=True, db_index=True)
    email2 = models.CharField(max_length=100, null=True)
    phone1 = models.CharField(max_length=15, null=True, db_index=True)
    phone2 = models.CharField(max_length=15, null=True)
    address_type = models.CharField(max_length=20, null=True)
    street1 = models.CharField(max_length=50, null=True)
    street2 = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=10, null=True)
    zip_code = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    class Meta:
        db_table = 'mainsite_address'

    @property
    def notes(self):
        return LinkNote.objects.filter(
            link_table='mainsite_address',
            link_id=self.id
        )

    def __str__(self):
        return '%s %s %s %s %s' % (self.address_type, self.street1, self.city, self.state, self.zip_code)


class Event(models.Model):
    name = models.CharField(max_length=50, db_index=True, default=str(datetime.date.today().year) + " summer retreat")
    address = models.ManyToManyField(Address)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return '%s' % self.name


class Registration(models.Model):
    event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)
    main_attendee = models.ForeignKey(Attendee, null=True, on_delete=models.SET_NULL)
    apply_type = models.CharField(max_length=20, null=True)
    apply_key = models.CharField(max_length=50, null=True)
    paid_x100 = models.IntegerField(default=0, null=True)
    total_x100 = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return '%s %s %s' % (self.title, self.main_attendee, self.total_x100)


class Attending(models.Model):
    registration = models.ForeignKey(Registration, null=True, on_delete=models.SET_NULL)
    attendee = models.ForeignKey(Attendee, null=True, on_delete=models.SET_NULL)
    price_x100 = models.IntegerField(default=100, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, null=True)
    attending_type = models.CharField(max_length=20, null=True)
    attending_program = models.CharField(max_length=30, null=True, db_index=True)
    belief = models.CharField(max_length=20, null=True)
    bed_needs = models.IntegerField(default=1)
    mobility = models.IntegerField(default=1000)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return '%s %s %s' % (self.attendee, self.attending_program, self.bed_needs)

