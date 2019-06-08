from django.contrib import admin

from mainsite.models import *

class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_type', 'street', 'city', 'zip_code', 'updated_at')

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_addresses', 'updated_at')

class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('chinese_name', 'english_name', 'updated_at')

class PriceAdmin(admin.ModelAdmin):
    list_display = ('price_label', 'price_type', 'start_date', 'price_value', 'updated_at')

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('main_attendee', 'apply_type', 'apply_key', 'event', 'updated_at')

class AttendingAdmin(admin.ModelAdmin):
    list_display = ('registration', 'attendee', 'price', 'bed_needs', 'updated_at')


admin.site.register(LinkNote)
admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Attending, AttendingAdmin)
