from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['note_counts'] = len(self.object.notes)
        data['note_class'] = '' if data['note_counts'] > 0 else 'd-none'
        return data
