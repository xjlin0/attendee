from django.views.generic.list import ListView
from mainsite.models import Attending


class AttendingView(ListView):
    model = Attending
    template_name = 'attendings/index.html'
    context_object_name = 'attendings'
    paginate_by = 100


    # def get_queryset(self):
    #     return Attending.objects.filter(created_by=self.request.user)
