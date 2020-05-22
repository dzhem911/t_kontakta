from django.urls import path
from . import views


app_name = 'our_contacts'

urlpatterns = [
    path('', views.OurContactss.as_view(), name='our_contacts'),
]