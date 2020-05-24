from django.shortcuts import render, redirect, get_object_or_404
from django.views import View, generic
from django.views.decorators.http import require_POST
from django.views.generic.base import RedirectView
from core.models import Tires
from .cart import Cart
from .forms import CartAddProductForm
from django.http import JsonResponse


@require_POST
def cart_add(request, product_vencode=None):
    cart = Cart(request)
    product = get_object_or_404(Tires, vencode=product_vencode)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

@require_POST
def cart_update_quantity(request, product_vencode):
    cart = Cart(request)
    product = get_object_or_404(Tires, vencode=product_vencode)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.update_quantity(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

@require_POST
def cart_add_this_page(request, product_vencode=None):
    cart = Cart(request)
    product = get_object_or_404(Tires, vencode=product_vencode)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('core:products')


def cart_remove(request, product_vencode):
    cart = Cart(request)
    product = get_object_or_404(Tires, vencode=product_vencode)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    form_class = CartAddProductForm
    return render(request, 'cart/detail.html', {'cart': cart, 'form_class': form_class})

