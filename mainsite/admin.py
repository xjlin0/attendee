from django.contrib import admin

from mainsite.models import *


class EventAddressAdmin(admin.ModelAdmin):
    list_display = ('event', 'address', 'updated_at')

class EventAddressInline(admin.TabularInline):
    model = EventAddress
    extra = 1


class AddressAdmin(admin.ModelAdmin):
    inlines = (EventAddressInline,)
    list_display = ('address_type', 'street', 'city', 'zip_code', 'updated_at')


class EventAdmin(admin.ModelAdmin):
    inlines = (EventAddressInline,)
    list_display = ('name', 'get_addresses', 'updated_at')


class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'last_name2', 'first_name2', 'updated_at')


class PriceAdmin(admin.ModelAdmin):
    list_display = ('price_label', 'price_type', 'start_date', 'price_value', 'updated_at')


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('main_attendee', 'apply_type', 'apply_key', 'event', 'updated_at')


class AttendingAdmin(admin.ModelAdmin):
    list_display = ('registration', 'attendee', 'price', 'division_names', 'bed_needs', 'updated_at')


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'info', 'updated_at')


class ProgramTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'program_group', 'display_order', 'updated_at')


class LinkNoteAdmin(admin.ModelAdmin):
    list_display = ('note_text', 'content_type', 'object_id', 'content_object', 'updated_at')


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'campus', 'updated_at')


class CampusAdmin(admin.ModelAdmin):
    list_display = ('name', 'address','updated_at')


class SuiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'site', 'updated_at')


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'label', 'suite', 'updated_at')


class ProgramGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'info', 'url', 'updated_at')


class ProgramProgressionAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_order', 'updated_at')


class ProgramSessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'program_group', 'program_progression', 'updated_at')


admin.site.register(LinkNote, LinkNoteAdmin)
admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(EventAddress, EventAddressAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Attending, AttendingAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Campus, CampusAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Suite, SuiteAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(ProgramGroup, ProgramGroupAdmin)
admin.site.register(ProgramProgression, ProgramProgressionAdmin)
admin.site.register(ProgramSession, ProgramSessionAdmin)
admin.site.register(ProgramTeam, ProgramTeamAdmin)
