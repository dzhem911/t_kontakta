from django.views import generic
from django.shortcuts import render
from .models import Tires, Photo, Category
from cart.forms import CartAddProductForm
from .filters import TireFilter
from django_filters.views import FilterView


class ProductList(FilterView):
    paginate_by = 10
    template_name = 'core/product_list.html'
    filterset_class = TireFilter
    form_class = CartAddProductForm


    def get_queryset(self):
        queryset = Tires.objects.filter(available=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['form'] = CartAddProductForm
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

