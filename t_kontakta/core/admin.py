from django.contrib import admin
from .models import Tires, Category, Photo

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)

class TiresAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('vencode',)}
    exclude = ['available']

admin.site.register(Tires, TiresAdmin)

admin.site.register(Photo)