from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.BootstrapFilterView, name='products'),
    #path('categories/<slug:category_slug>/', views.ProductView.as_view(), name='product_list_by_categories'),
    #path('item/<slug>/', views.ProductDetail.as_view(), name='product_detail'),

]