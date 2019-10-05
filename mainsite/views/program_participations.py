from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from mainsite.models import ProgramParticipation
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator([login_required], name='dispatch')
class ProgramParticipationListView(ListView):
    model = ProgramParticipation
    template_name = 'program_participations/index.html'


@method_decorator([login_required], name='dispatch')
class ProgramParticipationDetailView(DetailView):
    model = ProgramParticipation
    template_name = 'program_participations/show.html'


@method_decorator([login_required], name='dispatch')
class ProgramParticipationCreateView(CreateView):
    model = ProgramParticipation
    fields = [f.name for f in model._meta.fields if f.name not in ['created_at', 'updated_at']]
    template_name = 'program_participations/create_update.html'


@method_decorator([login_required], name='dispatch')
class ProgramParticipationUpdateView(UpdateView):
    model = ProgramParticipation
    fields = [f.name for f in model._meta.fields if f.name not in ['created_at', 'updated_at', 'status']]
    template_name = 'program_participations/create_update.html'