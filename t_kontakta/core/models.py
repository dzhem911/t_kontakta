from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField('Категория', max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True,
                            unique=True)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    """def get_absolute_url(self):
        return reverse('core:product_list_by_categories',
                       args=[self.slug])"""


class Photo(models.Model):
    name = models.ForeignKey('Tires', on_delete=models.SET_NULL, null=True, related_name='photos_name')
    photo = models.ImageField(upload_to='media/')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

    def __str__(self):
        return self.photo.url


class Tires(models.Model):
    vencode = models.CharField('Артикул', max_length=100, primary_key=True)
    slug = models.SlugField(max_length=100, db_index=True, verbose_name='Ссылка')
    price = models.DecimalField('Цена', max_digits=20, decimal_places=2)
    category = models.ManyToManyField(Category)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField(verbose_name="Процент износа (для новых значение 0)")
    radius = models.PositiveSmallIntegerField()
    weidth = models.PositiveSmallIntegerField()
    profile = models.PositiveSmallIntegerField()
    seasone = models.CharField(max_length=100, verbose_name='Сезонность')
    producer = models.CharField(max_length=150, verbose_name='Производитель')
    tire_model = models.CharField(max_length=150, verbose_name='Модель')

    class Meta:
        verbose_name = "Шина"
        verbose_name_plural = "Шины"

    def __str__(self):
        return f'{self.producer} - {self.tire_model}'

    def __iter__(self):
        pass


    def get_absolute_url(self):
        return reverse('core:product_detail', args=[str(self.slug)])