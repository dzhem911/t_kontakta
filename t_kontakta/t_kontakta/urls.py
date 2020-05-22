from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

import debug_toolbar

urlpatterns = [
    path('mouse/', admin.site.urls),
    path('', include('core.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('tire_service/', include('tire_service.urls')),
    path('contacts/', include('our_contacts.urls')),
    path('about_us/', include('about_us.urls')),
    path('tinymce/', include('tinymce.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]