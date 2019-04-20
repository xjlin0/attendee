from django.contrib import admin

from mainsite.models import *

class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_type', 'street1', 'city', 'zip_code', 'updated_at')

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_addresses', 'updated_at')

admin.site.register(LinkNote)
admin.site.register(Attendee)
admin.site.register(Address, AddressAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Price)
admin.site.register(Registration)
admin.site.register(Attending)
