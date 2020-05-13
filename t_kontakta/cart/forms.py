from django import forms
from cart.cart import Cart

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 101)]



class CartAddProductForm(forms.Form):
    #quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label='Количество')
    quantity = forms.IntegerField(label='Количество:', initial=1, min_value=1)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class CartQuantity(forms.Form):
    quantity = forms.IntegerField(label='Количество:', initial=1, min_value=1)