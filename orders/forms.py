from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя ', max_length=100)
    last_name = forms.CharField(label='Фамилия', max_length=100, required=False)
    email = forms.EmailField(label='Email', max_length=100)
    phone_number = forms.CharField(label='Номер телефона', min_length=16, max_length=16)
    address = forms.CharField(label='Адрес доставки ', max_length=200, required=False)
    postal_code = forms.CharField(label='Индекс', max_length=15, required=False)
    city = forms.CharField(label='Город', max_length=50, required=False)
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'postal_code', 'city']