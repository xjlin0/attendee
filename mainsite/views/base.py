from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('base/index.html')
    context = {
        'base_value': 555,
    }
    return HttpResponse(template.render(context, request))
