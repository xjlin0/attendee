from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from mainsite.models import Attending
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Count, Sum


@method_decorator([login_required], name='dispatch')
class AttendingListView(ListView):
    model = Attending
    template_name = 'attendings/index.html'
    paginate_by = 100

    # # def get_queryset(self):
    # #     # original qs
    # #     qs = super().get_queryset()
    # #     # filter by a variable captured from url, for example
    # #     return qs.filter(name__startswith=self.kwargs['name'])
    #
    #
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        #breakpoint()
        data['bed_counts'] = self.object_list.aggregate(Sum('bed_needs'))['bed_needs__sum']
        division_counts = self.object_list.values('divisions__name').annotate(total=Count('id')).order_by('divisions__name')
        data['division_counts'] = ', '.join([f"{dc['divisions__name']}: {dc['total']}" for dc in division_counts])
        return data


    # def get_queryset(self):
    #     return self.object_list.filter(deleted_on__isnull=False)


@method_decorator([login_required], name='dispatch')
class AttendingDetailView(DetailView):
    model = Attending
    template_name = 'attendings/show.html'


@method_decorator([login_required], name='dispatch')
class AttendingUpdateView(UpdateView):
    model = Attending
    fields = [f.name for f in model._meta.fields if f.name not in ['created_at', 'updated_at', 'status']]
    template_name = 'attendings/create_update.html'