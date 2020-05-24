from django import forms
from .models import Category, Tires
from django.forms.widgets import Select
from .models import Tires


"""class PhotosForm(forms.ModelForm):
    photos = forms.ImageField(label=u'Фотографии', widget=forms.FileInput(attrs={'multiple': 'multiple'}))"""