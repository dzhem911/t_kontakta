from django.contrib import admin
from .models import Tires, Category, Photo
from .forms import PhotosForm

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

admin.site.register(Tires, TiresAdmin)
