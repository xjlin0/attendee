from django.http import HttpResponse
from django.template import loader
#from django.views.generic import ListView


def index(request):
    template = loader.get_template('attendings/index.html')
    context = {
        'price': 777,
    }
    return HttpResponse(template.render(context, request))
