# Generated by Django 2.2.6 on 2019-10-22 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Модель автомобіля')),
                ('slug', models.SlugField(max_length=32)),
            ],
            options={
                'verbose_name': 'Модель автомобіля',
                'verbose_name_plural': 'Моделі автомобілів',
            },
        ),
        migrations.CreateModel(
            name='VehicleInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Актив/Неактив')),
                ('title', models.CharField(blank=True, max_length=64, verbose_name='Назва')),
                ('image', models.ImageField(upload_to='test_img/', verbose_name='Зображення')),
                ('price_usd', models.CharField(max_length=32, verbose_name='Ціна в у.о.')),
                ('price_uah', models.CharField(blank=True, max_length=32, verbose_name='Ціна в грн.')),
                ('mileage', models.CharField(max_length=32, verbose_name='Пробіг')),
                ('city', models.CharField(max_length=32, verbose_name='Місто')),
                ('fuel', models.IntegerField(choices=[(1, 'Дизель'), (2, 'Бензин'), (3, 'Газ/Бензин'), (4, 'Електро'), (5, 'Гібрид')], verbose_name='Тип пального')),
                ('gearbox', models.IntegerField(choices=[(1, 'Ручна'), (2, 'Автоматична')], verbose_name='Тип КПП')),
                ('numberplate', models.CharField(max_length=8, verbose_name='Номери')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Створено')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Оновлено')),
            ],
            options={
                'verbose_name': 'Оголошення',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Марка автомобіля', 'verbose_name_plural': 'Автомобільні марки'},
        ),
        migrations.AlterModelOptions(
            name='testvehicle',
            options={'verbose_name': 'Just for test'},
        ),
        migrations.AlterField(
            model_name='brand',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Category'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.SlugField(max_length=32),
        ),
        migrations.AlterField(
            model_name='brand',
            name='title',
            field=models.CharField(max_length=32, verbose_name='Марка автомобіля'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=32),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=32, verbose_name='Категорія'),
        ),
        migrations.DeleteModel(
            name='VehicleType',
        ),
        migrations.AddField(
            model_name='vehicleinstance',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Brand'),
        ),
        migrations.AddField(
            model_name='vehicleinstance',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Category'),
        ),
        migrations.AddField(
            model_name='vehicleinstance',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Type'),
        ),
        migrations.AddField(
            model_name='vehicleinstance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач'),
        ),
        migrations.AddField(
            model_name='type',
            name='brand',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='category', chained_model_field='category', on_delete=django.db.models.deletion.CASCADE, to='main.Brand'),
        ),
        migrations.AddField(
            model_name='type',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Category'),
        ),
    ]
