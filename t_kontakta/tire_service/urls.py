from django.urls import path
from . import views

app_name = 'tire_service'

urlpatterns = [
    path('', views.ServiceDetail.as_view(), name='tire_service'),
]