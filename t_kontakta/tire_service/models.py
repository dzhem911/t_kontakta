from django.db import models

class Service(models.Model):
    service = models.CharField(verbose_name='Услуга', max_length=100)
    description = models.TextField(verbose_name='Описание', max_length=1000)
    price = models.DecimalField('Цена', max_digits=20, decimal_places=2)

    def __str__(self):
        return f'{self.service}'


    class Meta:
        verbose_name = 'Шиномонтаж'
        verbose_name_plural = 'Шиномонтаж'
