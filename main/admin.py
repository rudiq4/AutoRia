from django.contrib import admin
from .models import Category, Brand, VehicleType, TestVehicle


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class BrandAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ['brand', 'title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class TestVehicleAdmin(admin.ModelAdmin):
    list_display = ['title', 'price_usd', 'price_uah', 'mileage', 'city', 'fuel', 'gearbox', 'numberplate']


admin.site.register(TestVehicle, TestVehicleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(VehicleType, VehicleTypeAdmin)

