from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Article

class AboutUs(TemplateView):
    template_name = 'about_us/about_us.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super(AboutUs, self).get_context_data(**kwargs)
        context['article'] = Article.objects.all()
        return context