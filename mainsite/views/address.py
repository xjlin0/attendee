from django.views.generic.list import ListView
from mainsite.models import Address
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator([login_required], name='dispatch')
class AddressListView(ListView):
    model = Address
    template_name = 'addresses/index.html'
