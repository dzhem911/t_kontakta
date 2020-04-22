from django.contrib import admin
from .models import Tires, Category, Photo

class PhotoAdmin(admin.StackedInline):
    model = Photo

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)

class TiresAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('vencode',)}
    exclude = ['available']
    inlines = [PhotoAdmin]
    list_display = ['producer', 'tire_model', 'price', 'stock']
    list_editable = ['price', 'stock']

admin.site.register(Tires, TiresAdmin)
