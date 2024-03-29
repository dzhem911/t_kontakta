from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<str:product_vencode>', views.cart_add, name='cart_add'),
    path('remove/<str:product_vencode>', views.cart_remove, name='cart_remove'),
    path('update_quantity/<str:product_vencode>', views.cart_update_quantity, name='cart_update_quantity'),
]