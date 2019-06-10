from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from mainsite.models import Address
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator([login_required], name='dispatch')
class AddressListView(ListView):
    model = Address
    template_name = 'addresses/index.html'


@method_decorator([login_required], name='dispatch')
class AddressDetailView(DetailView):
    model = Address
    template_name = 'addresses/detail.html'


@method_decorator([login_required], name='dispatch')
class AddressCreateView(CreateView):
    model = Address
    fields = ['email1', 'email2', 'phone1', 'phone2', 'address_type', 'street1', 'street2', 'city', 'state', 'zip_code']
    template_name = 'addresses/create.html'
    success_url = '/addresses/'
