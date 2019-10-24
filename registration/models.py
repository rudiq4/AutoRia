from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from main.models import VehicleInstance


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Користувач")
    email = models.EmailField('e-mail')
    # phone = models.CharField('Номер телефону', max_length=13)
    posts = models.ForeignKey(VehicleInstance, on_delete=models.CASCADE, verbose_name='Оголошення автора')

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('customer:account', kwargs={'user': self.user.username})
