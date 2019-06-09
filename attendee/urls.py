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
from mainsite.views import AttendingListView, AttendingDetailView, BaseView, AddressListView, AddressDetailView, LinkNoteDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('', TemplateView.as_view(template_name='base/index.html'), name='home'),
    path('', BaseView.as_view(), name='home'),
    path('link_note/<int:pk>/', login_required(LinkNoteDetailView.as_view()), name='link_note_detail'),
    path('addresses/', login_required(AddressListView.as_view()), name='addresses'),
    path('addresses/<int:pk>/', login_required(AddressDetailView.as_view()), name='address_detail'),
    path('attendings/', login_required(AttendingListView.as_view()), name='attendings'),
    path('attendings/<int:pk>/', login_required(AttendingDetailView.as_view()), name='attending_detail'),
]
