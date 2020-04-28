from django.views import generic
from django.shortcuts import render
from .models import Tires, Photo, Category
from cart.forms import CartAddProductForm
from .forms import MyChoice
from django.db.models import Q


class ProductList(generic.ListView):
    paginate_by = 9
    template_name = 'core/product_list.html'
    form = MyChoice()

    def is_valid_queryparam(self, param):
        return param !='' and param !='Выбрать' and param is not None


    def get_queryset(self):
        queryset = Tires.objects.filter(available=True)


        if self.request.GET.get('category') and self.request.GET.get('category')!='Выбрать':
            queryset = Tires.objects.filter(category__name__icontains=self.request.GET.get('category'))
        if self.request.GET.get('producer') and self.request.GET.get('producer')!='Выбрать':
            queryset = Tires.objects.filter(producer__icontains=self.request.GET.get('producer'))
        if self.request.GET.get('tire_model') and self.request.GET.get('tire_model')!='Выбрать':
            queryset = Tires.objects.filter(tire_model__icontains=self.request.GET.get('tire_model'))
        if self.request.GET.get('radius') and self.request.GET.get('radius')!='Выбрать':
            queryset = Tires.objects.filter(radius__icontains=self.request.GET.get('radius'))
        if self.request.GET.get('status') and self.request.GET.get('status')!='Выбрать':
            queryset = Tires.objects.filter(status__icontains=self.request.GET.get('status'))
        if self.request.GET.get('profile') and self.request.GET.get('profile')!='Выбрать':
            queryset = Tires.objects.filter(profile__icontains=self.request.GET.get('profile'))

        """if self.request.GET.get('category') and self.request.GET.get('producer') and self.request.GET.get('tire_model') \
            or self.request.GET.get('radius') and self.request.GET.get('status') and self.request.GET.get('profile') \
                and self.request.GET.get('status')!='Выбрать' and  self.request.GET.get('profile')!='Выбрать':
            queryset =  Tires.objects.filter(Q(category__name=self.request.GET.get('category')) |
                                             Q(producer=self.request.GET.get('producer')) |
                                             Q(tire_model=self.request.GET.get('tire_model')) |
                                             Q(radius=self.request.GET.get('radius')) |
                                             Q(status=self.request.GET.get('status')) |
                                             Q(profile=self.request.GET.get('profile'))
                                             )"""

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['queryset'] = Tires.objects.filter(available=True)
        context['qphoto'] = Photo.objects.all()
        context['categories'] = Category.objects.all()
        context['uniq_producer'] = Tires.objects.order_by('producer').distinct('producer')
        context['uniq_tire_model'] = Tires.objects.order_by('tire_model').distinct('tire_model')
        context['uniq_radius'] = Tires.objects.order_by('radius').distinct('radius')
        context['uniq_status'] = Tires.objects.order_by('status').distinct('status')
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

