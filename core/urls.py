from django.urls import path
from . import views
from cart import views as cart_views

app_name = 'core'

urlpatterns = [
    path('', views.ProductList.as_view(), name='products'),
    path('item/<slug>/', views.ProductDetail.as_view(), name='product_detail'),
    path('add/<str:product_vencode>', cart_views.cart_add_this_page, name='cart_add_this_page'),
]