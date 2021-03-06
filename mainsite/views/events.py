from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from mainsite.models import Event
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator([login_required], name='dispatch')
class EventListView(ListView):
    model = Event
    template_name = 'events/index.html'
    paginate_by = 100

    # # def get_queryset(self):
    # #     # original qs
    # #     qs = super().get_queryset()
    # #     # filter by a variable captured from url, for example
    # #     return qs.filter(name__startswith=self.kwargs['name'])


@method_decorator([login_required], name='dispatch')
class EventDetailView(DetailView):
    model = Event
    template_name = 'events/show.html'


@method_decorator([login_required], name='dispatch')
class EventCreateView(CreateView):
    model = Event
    fields = [f.name for f in model._meta.fields if f.name not in ['created_at', 'updated_at']]
    template_name = 'events/create_update.html'

    # def form_valid(self, form):
    #     self.object = form.save()
    #     # do something with self.object
    #     # remember the import: from django.http import HttpResponseRedirect
    #     return HttpResponseRedirect(self.get_success_url())

    #
    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.user = self.request.user
    #     self.object.save()
    #     return HttpResponseRedirect(self.get_success_url())


@method_decorator([login_required], name='dispatch')
class EventUpdateView(UpdateView):
    model = Event
    fields = [f.name for f in model._meta.fields if f.name not in ['created_at', 'updated_at', 'status']]
    template_name = 'events/create_update.html'