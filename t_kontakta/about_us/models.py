from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'