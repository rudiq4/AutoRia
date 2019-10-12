from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Користувач")
    email = models.EmailField(verbose_name='e-mail')

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('customer:account', kwargs={'user': self.user.username})
