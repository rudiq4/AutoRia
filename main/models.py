from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Category(models.Model):
    title = models.CharField(max_length=32, verbose_name='Категорія')
    slug = models.SlugField(max_length=32)

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        pass
        # return reverse('shop:ProductListByCategory', args=[self.slug])

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=32, verbose_name='Марка автомобіля')
    slug = models.SlugField(max_length=32)

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        pass
        # return reverse('shop:ProductListByCategory', args=[self.slug])

    class Meta:
        verbose_name = 'Марка автомобіля'
        verbose_name_plural = 'Автомобільні марки'


class Type(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = ChainedForeignKey(
        'Brand',
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True
    )
    title = models.CharField(max_length=32, verbose_name='Модель автомобіля')
    slug = models.SlugField(max_length=32)

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        pass
        # return reverse('shop:ProductListByCategory', args=[self.slug])

    class Meta:
        verbose_name = 'Модель автомобіля'
        verbose_name_plural = 'Моделі автомобілів'


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


class VehicleInstance(models.Model):
    pass
#  Тут буде конкретний екземпляр моделі
