"""attendee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required, permission_required
# from django.views.generic.base import TemplateView
from mainsite.views import AttendingListView,\
                           AttendingDetailView,\
                           AttendingUpdateView,\
                           BaseView,\
                           AddressListView,\
                           AddressDetailView,\
                           AddressCreateView,\
                           AddressUpdateView,\
                           LinkNoteDetailView,\
                           EventListView,\
                           EventDetailView,\
                           EventCreateView,\
                           EventUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),

    # path('', TemplateView.as_view(template_name='base/index.html'), name='home'),
    path('', BaseView.as_view(), name='home'),

    path('link_note/<int:pk>/', login_required(LinkNoteDetailView.as_view()), name='link_note_detail'),

    path('events/', login_required(EventListView.as_view()), name='events'),
    path('events/new', login_required(EventCreateView.as_view()), name='events_new'),
    path('events/<int:pk>/edit', login_required(EventUpdateView.as_view()), name='events_update'),
    path('events/<int:pk>/', login_required(EventDetailView.as_view()), name='event_detail'),

    path('addresses/', login_required(AddressListView.as_view()), name='addresses'),
    path('addresses/new', login_required(AddressCreateView.as_view()), name='addresses_new'),
    path('addresses/<int:pk>/edit', login_required(AddressUpdateView.as_view()), name='address_update'),
    path('addresses/<int:pk>/', login_required(AddressDetailView.as_view()), name='address_detail'),

    path('attendings/', login_required(AttendingListView.as_view()), name='attendings'),
    path('attendings/<int:pk>/edit', login_required(AttendingUpdateView.as_view()), name='attending_update'),
    path('attendings/<int:pk>/', login_required(AttendingDetailView.as_view()), name='attending_detail'),
]
