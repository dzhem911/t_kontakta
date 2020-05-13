from django.views.generic.base import TemplateView
from django.shortcuts import render
from .models import Service

"""def tire_service(request):
    service = Service(request)
    return render(request, 'tire_service/desc.html', {'service': service})"""


class ServiceDetail(TemplateView):
    template_name = 'tire_service/desc.html'
    model = Service

    def get_context_data(self, **kwargs):
        context = super(ServiceDetail, self).get_context_data(**kwargs)
        context['service'] = Service.objects.all()
        return context