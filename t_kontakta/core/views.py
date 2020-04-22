from django.views import generic
from django.shortcuts import render
from .models import Tires, Photo
from cart.forms import CartAddProductForm


class ProductList(generic.ListView):
    paginate_by = 5
    template_name = 'core/product_list.html'

    def get_queryset(self):
        return Tires.objects.filter(available=True)

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['queryset'] = Tires.objects.filter(available=True)
        context['qphoto'] = Photo.objects.all()
        return context


class ProductDetail(generic.DetailView):
    slug_field = 'slug'
    template_name = 'core/product_view.html'
    form_class = CartAddProductForm
    model = Tires

    def get_queryset(self):
        return Tires.objects.filter(available=True)

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['form'] = CartAddProductForm
        return context

