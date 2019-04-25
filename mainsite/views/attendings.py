from django.http import HttpResponse
from django.template import loader

def attendings(request):
    template = loader.get_template('attendings.html')
    context = {
        'price': 77,
    }
    return HttpResponse(template.render(context, request))
