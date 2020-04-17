from django.shortcuts import render
from .models import Tires, Photo

def BootstrapFilterView(request):
    qs = Tires.objects.all()
    qs_photo = Photo.objects.all()

    context = {
        'queryset': qs,
        'qphoto': qs_photo,
    }

    return render(request, 'core/product_list.html', context)