import django_filters

from .models import Tires, Category, Photo

class CharFilterInFilter(django_filters.BaseInFilter, django_filters.CharFilter):
    pass

class TireFilter(django_filters.FilterSet):

    def __init__(self, *args, **kwargs):
        super(TireFilter, self).__init__(*args, **kwargs)


    category_query = Category.objects.values_list('name', flat=True).distinct()
    producer_query = Tires.objects.values_list('producer', flat=True).distinct()
    tire_model_query = Tires.objects.values_list('tire_model', flat=True).order_by('tire_model').distinct()
    status_query = Tires.objects.values_list('status', flat=True).order_by('status').distinct()
    radius_query = Tires.objects.values_list('radius', flat=True).order_by('radius').distinct()
    weidth_query = Tires.objects.values_list('weidth', flat=True).order_by('weidth').distinct()
    profile_query = Tires.objects.values_list('profile', flat=True).order_by('profile').distinct()
    seasone_query = Tires.objects.values_list('seasone', flat=True).order_by('seasone').distinct()
    producer_query_choices = [(id, id) for id in producer_query]


    def query_choices(self):
        qchoices = [(id, id) for id in self]
        return qchoices


    category =  django_filters.ChoiceFilter(field_name='category__name', choices=query_choices(category_query),
                                            label='Категория', empty_label='Все') # CharFilterInFilter(field_name='category__name')
    producer = django_filters.ChoiceFilter(field_name='producer', choices=query_choices(producer_query),
                                           label='Марка', empty_label='Все')
    tire_model = django_filters.ChoiceFilter(field_name='tire_model',
                                           choices=query_choices(tire_model_query), empty_label='Все')  # lookup_expr by default is'='
    status = django_filters.ChoiceFilter(field_name='status', choices=query_choices(status_query),
                                         label='Состояние', empty_label='Любое', help_text='% износа продукта. Для новых, значение = 0')
    radius = django_filters.ChoiceFilter(field_name='radius', choices=query_choices(radius_query),
                                         label='Радиус', empty_label='Любой')
    weidth = django_filters.ChoiceFilter(field_name='weidth', choices=query_choices(weidth_query),
                                         label='Ширина', empty_label='Все')
    profile = django_filters.ChoiceFilter(field_name='profile', choices=query_choices(profile_query),
                                          label='Профиль', empty_label='Все')
    seasone = django_filters.ChoiceFilter(field_name='seasone', choices=query_choices(seasone_query),
                                          label='Сезонность', empty_label='Все')


    class Meta:
        model = Tires
        fields = ['category', 'producer', 'tire_model', 'status', 'radius', 'weidth', 'profile', 'seasone', ]
        #exclude = [field.name for field in Tires._meta.fields]
        #order_by_field = 'tire_model'