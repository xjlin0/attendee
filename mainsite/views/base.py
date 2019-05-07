from django.shortcuts import render
from django.views import View


class BaseView(View):
    template_name = 'base/index.html'
    context = {
        'base_value': 555,
    }

    def get(self, request):
        return render(request, self.template_name, self.context)
