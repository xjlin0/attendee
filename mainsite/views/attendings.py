from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.shortcuts import render
#from django.views.generic import ListView


# def index(request):
class AttendingView(View):
    template_name = 'attendings/index.html'
    context = {
        'price': 777,
    }

    def get(self, request):
        return render(request, self.template_name, self.context)
#     return HttpResponse(template.render(context, request))
