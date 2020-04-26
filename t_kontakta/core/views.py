from django.views import generic
from django.shortcuts import render
from .models import Tires, Photo, Category
from cart.forms import CartAddProductForm
from .forms import MyChoice


class ProductList(generic.ListView):
    paginate_by = 9
    template_name = 'core/product_list.html'
    form = MyChoice()


    def get_queryset(self):
        queryset = Tires.objects.filter(available=True)

        if self.request.GET.get('radius'):
            queryset = Tires.objects.filter(radius=self.request.GET.get('radius'))
        if self.request.GET.get('category'):
            queryset = Tires.objects.filter(category__name=self.request.GET.get('category'))
        if self.request.GET.get('category'):
            queryset = Tires.objects.filter(status=self.request.GET.get('status'))

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['queryset'] = Tires.objects.filter(available=True)
        context['qphoto'] = Photo.objects.all()
        context['categories'] = Category.objects.all()
        context['form'] = self.form
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

