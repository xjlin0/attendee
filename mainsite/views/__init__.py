# from .attendings import index as attendings_index
from .attendings import AttendingListView, AttendingDetailView, AttendingUpdateView
from .address import AddressListView, AddressDetailView, AddressCreateView, AddressUpdateView
from .events import EventListView, EventDetailView, EventCreateView, EventUpdateView
from .link_note import LinkNoteDetailView
from .base import BaseView
