from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey


class Category(models.Model):
    title = models.CharField('Категорія', max_length=32)
    slug = models.SlugField(max_length=32)

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        pass

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField('Марка автомобіля', max_length=32)
    slug = models.SlugField(max_length=32)

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        pass

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
    title = models.CharField('Модель автомобіля', max_length=32)
    slug = models.SlugField(max_length=32)

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        pass

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
    title = models.CharField('Назва автомобіля', max_length=32)
    image = models.ImageField('Зображення', upload_to='test_img/')
    price_usd = models.CharField('Ціна в у.о.', max_length=32)
    price_uah = models.CharField('Ціна в грн.', max_length=32)
    mileage = models.CharField('Пробіг', max_length=32)
    city = models.CharField('Місто', max_length=32)
    fuel = models.IntegerField('Тип пального', choices=FUEL_CHOICE)
    gearbox = models.IntegerField('Тип КПП', choices=GEARBOX_CHOICE)
    numberplate = models.CharField('Номери', max_length=8)

    class Meta:
        verbose_name = 'Just for test'

    def __str__(self):
        return self.title


class VehicleInstance(models.Model):
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    is_active = models.BooleanField('Актив/Неактив', default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    image = models.ImageField('Зображення', upload_to='test_img/')
    price_usd = models.CharField('Ціна в у.о.', max_length=32)
    price_uah = models.CharField('Ціна в грн.', max_length=32)
    mileage = models.CharField('Пробіг', max_length=32)
    city = models.CharField('Місто', max_length=32)
    fuel = models.IntegerField('Тип пального', choices=FUEL_CHOICE)
    gearbox = models.IntegerField('Тип КПП', choices=GEARBOX_CHOICE)
    numberplate = models.CharField('Номери', max_length=8)
    created = models.DateTimeField('Створено', auto_now_add=True)
    updated = models.DateTimeField('Оновлено', auto_now=True)

    class Meta:
        verbose_name = 'Оголошення'

    def __str__(self):
        return str(self.id)
