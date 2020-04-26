from django import forms
from .models import Category, Tires
from django.forms import ChoiceField

class PhotosForm(forms.ModelForm):
    #name = forms.CharField(label=u'Продукт')
    photos = forms.ImageField(label=u'Фотографии', widget=forms.FileInput(attrs={'multiple': 'multiple'}))

class MyChoice(forms.ModelForm):
    status = forms.IntegerField()


    class Meta:
        model = Tires
        fields = ['status']
