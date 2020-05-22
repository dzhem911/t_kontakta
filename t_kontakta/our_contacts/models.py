from django.db import models
from tinymce.models import HTMLField


class OurContacts(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = HTMLField()
    img = models.ImageField(upload_to='media/', verbose_name='Изображение', null=True, blank=True)
    phone_number = models.CharField(max_length=11, verbose_name='Номер телефона')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'