from django.contrib import admin
from .models import TestVehicle, Category, Brand, Type, VehicleInstance


class TestVehicleAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_usd', 'price_uah', 'mileage', 'city', 'fuel', 'gearbox', 'numberplate')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    prepopulated_fields = {'slug': ('title',)}


class TypeAdmin(admin.ModelAdmin):
    list_display = ('category', 'brand', 'title')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)  # just 4 tests
    list_filter = ('title',)  # just 4 tests


class VehicleInstanceAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'type', 'image', 'price_usd', 'price_uah',
        'mileage', 'city', 'fuel', 'gearbox', 'numberplate')
    exclude = ('title', 'price_uah')


admin.site.register(TestVehicle, TestVehicleAdmin)
admin.site.register(VehicleInstance, VehicleInstanceAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
