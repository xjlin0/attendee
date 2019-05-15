from django.views.generic.list import ListView
from mainsite.models import Attending
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.db.models import Count


class_decorators = [login_required]


@method_decorator(class_decorators, name='dispatch')
class AttendingView(ListView):
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
        program_counts = self.object_list.values('attending_program').annotate(total=Count('attending_program'))
        data['program_counts'] = ', '.join([program_count['attending_program']+': ' + str(program_count['total']) for program_count in program_counts])
        return data


    # def get_queryset(self):
    #     return self.object_list.filter(deleted_on__isnull=False)
