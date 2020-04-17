from django import forms

class PhotosForm(forms.ModelForm):
    #name = forms.CharField(label=u'Продукт')
    photos = forms.ImageField(label=u'Фотографии', widget=forms.FileInput(attrs={'multiple': 'multiple'}))