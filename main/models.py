from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=32, verbose_name='Категорія', db_index=True)
    slug = models.SlugField(max_length=32, db_index=True, unique=True)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass
        # return reverse('shop:ProductListByCategory', args=[self.slug])


class Brand(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категорія', on_delete=models.CASCADE)
    title = models.CharField(max_length=32, verbose_name='Виробник', db_index=True)
    slug = models.SlugField(max_length=32, db_index=True, unique=True)

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марка'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass
        # return reverse('shop:ProductListByCategory', args=[self.slug])


class VehicleType(models.Model):
    brand = models.ForeignKey(Brand, verbose_name='Виробник', on_delete=models.CASCADE)
    title = models.CharField(max_length=32, verbose_name='Модель', db_index=True)
    slug = models.SlugField(max_length=32, db_index=True, unique=True)

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Моделі'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass
        # return reverse('shop:ProductListByCategory', args=[self.slug])


class Vehicle(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категорія', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, verbose_name='Марка', on_delete=models.CASCADE)
    vehicle_type = models.ForeignKey(VehicleType, verbose_name='Модель', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Автомобіль'
        verbose_name_plural = 'Автомобілі'

    def __str__(self):
        return '{} {}'.format(self.brand, self.vehicle_type)

    def get_absolute_url(self):
        pass
        # return reverse('shop:ProductListByCategory', args=[self.slug])


class TestVehicle(models.Model):
    FUEL_CHOICE = (
        (1, 'Дизель'),
        (2, 'Бензин'),
        (3, 'Газ/Бензин'),
        (4, 'Електро'),
        (5, 'Гібрид'),
    )
    GEARBOX_CHOICE = (
        (1, 'Ручна'),
        (2, 'Автоматична'),
    )
    title = models.CharField(max_length=32, verbose_name='Назва автомобіля')
    image = models.ImageField(upload_to='test_img/', verbose_name='Зображення')
    price_usd = models.CharField(max_length=32, verbose_name='Ціна в у.о.')
    price_uah = models.CharField(max_length=32, verbose_name='Ціна в грн.')
    mileage = models.CharField(max_length=32, verbose_name='Пробіг')
    city = models.CharField(max_length=32, verbose_name='Місто')
    fuel = models.IntegerField(choices=FUEL_CHOICE, verbose_name='Тип пального')
    gearbox = models.IntegerField(choices=GEARBOX_CHOICE, verbose_name='Тип КПП')
    numberplate = models.CharField(max_length=8, verbose_name='Номери')

    class Meta:
        verbose_name = 'Тестова штучка'

    def __str__(self):
        return self.title
