# Generated by Django 3.0.2 on 2020-04-17 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Фото', 'verbose_name_plural': 'Фото'},
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photos_name', to='core.Tires'),
        ),
        migrations.AlterField(
            model_name='tires',
            name='status',
            field=models.PositiveSmallIntegerField(verbose_name='Процент износа (для новых значение 0)'),
        ),
    ]
