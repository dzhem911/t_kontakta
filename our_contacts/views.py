from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import OurContacts


class OurContactss(TemplateView):
    template_name = 'our_contacts/our_contacts.html'
    model = OurContacts

    def get_context_data(self, **kwargs):
        context = super(OurContactss, self).get_context_data(**kwargs)
        context['contacts'] = OurContacts.objects.all()
        return context