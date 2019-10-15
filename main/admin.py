from django.contrib import admin
from .models import TestVehicle, Category, Brand, Type


class TestVehicleAdmin(admin.ModelAdmin):
    list_display = ['title', 'price_usd', 'price_uah', 'mileage', 'city', 'fuel', 'gearbox', 'numberplate']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    prepopulated_fields = {'slug': ('title',)}


class TypeAdmin(admin.ModelAdmin):
    list_display = ('category', 'brand', 'title')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(TestVehicle, TestVehicleAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
