from django.contrib import admin

from mainsite.models import *


class EventAddressAdmin(admin.ModelAdmin):
    list_display = ('event', 'address', 'updated_at')


class EventAddressInline(admin.TabularInline):
    model = EventAddress
    extra = 0


class AddressAdmin(admin.ModelAdmin):
    inlines = (EventAddressInline,)
    list_display = ('address_type', 'street', 'city', 'zip_code', 'phone1', 'email1')


class AttendingAddressInline(admin.StackedInline):
    model = AttendingAddress
    extra = 0


class DivisionAdmin(admin.ModelAdmin):
    list_display = ('organization', 'name', 'key', 'updated_at')


class AttendingDivisionInline(admin.StackedInline):
    model = AttendingDivision
    extra = 0


class EventAdmin(admin.ModelAdmin):
    inlines = (EventAddressInline,)
    list_display = ('name', 'get_addresses', 'updated_at')


class AttendeeAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'last_name2', 'first_name2')
    list_display = ('first_name', 'last_name', 'last_name2', 'first_name2', 'updated_at')


class PriceAdmin(admin.ModelAdmin):
    list_display = ('price_label', 'price_type', 'start_date', 'price_value', 'updated_at')


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('main_attendee', 'apply_type', 'apply_key', 'event', 'updated_at')


class ProgramParticipationAdmin(admin.ModelAdmin):
    # list_filter = ('program_session', 'attending', 'character', 'program_team')
    list_display = ('brief_program_session', 'attending', 'character', 'program_team', 'updated_at')


class ProgramParticipationInline(admin.StackedInline):
    model = ProgramParticipation
    extra = 0


class AttendingAdmin(admin.ModelAdmin):
    search_fields = ('attendee__first_name', 'attendee__last_name', 'attendee__first_name2', 'attendee__first_name2')
    inlines = (AttendingDivisionInline, AttendingAddressInline, ProgramParticipationInline,)
    list_display = ('registration', 'attendee', 'price', 'division_names', 'bed_needs', 'all_addresses')


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


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at')


class RelationshipAdmin(admin.ModelAdmin):
    list_display = ('from_attendee', 'to_attendee', 'relation', 'updated_at')


class ProgramGroupAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'info', 'url', 'updated_at')


class ProgramProgressionAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'display_order', 'updated_at')


class ProgramSessionAdmin(admin.ModelAdmin):
    inlines = (ProgramParticipationInline,)
    search_fields = ('program_group__name', 'program_progression__name', 'name')
    # list_filter = ('program_group', 'program_progression')
    list_display = ('program_group', 'program_progression', 'start_at', 'name', 'location', 'updated_at')


class ProgramGroupSettingAdmin(admin.ModelAdmin):
    list_display = ('program_group', 'schedules', 'start_time', 'duration', 'location', 'updated_at')


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
admin.site.register(Division, DivisionAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Relationship, RelationshipAdmin)
admin.site.register(ProgramGroup, ProgramGroupAdmin)
admin.site.register(ProgramProgression, ProgramProgressionAdmin)
admin.site.register(ProgramSession, ProgramSessionAdmin)
admin.site.register(ProgramTeam, ProgramTeamAdmin)
admin.site.register(ProgramParticipation, ProgramParticipationAdmin)
admin.site.register(ProgramGroupSetting, ProgramGroupSettingAdmin)

