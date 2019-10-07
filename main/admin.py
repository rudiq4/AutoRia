from django.contrib import admin
from .models import Category, Brand, VehicleType, Vehicle


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class BrandAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ['brand', 'title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class VehicleAdmin(admin.ModelAdmin):
    list_display = ['category', 'brand', 'vehicle_type']



# class ProductAdmin(admin.ModelAdmin):
#     list_display = [
#         'name', 'slug', 'price',
#         'available', 'created', 'updated'
#     ]
#     list_editable = [
#         'price', 'available'
#     ]
#     prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(VehicleType, VehicleTypeAdmin)
admin.site.register(Vehicle, VehicleAdmin)
