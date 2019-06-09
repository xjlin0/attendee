from django.views.generic.detail import DetailView
from mainsite.models import LinkNote
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator([login_required], name='dispatch')
class LinkNoteDetailView(DetailView):
    model = LinkNote
    # template_name = 'note/detail.html'
