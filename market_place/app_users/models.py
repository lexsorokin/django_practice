from django.contrib.auth.models import User
from django.db import models
from app_market_place.models import Goods


class Profile(models.Model):
    STATUS_CHOICES = [
        ('b', 'Basic'),
        ('v', 'VIP')
    ]
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name='Имя', max_length=100, null=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=100, null=True)
    email = models.EmailField(verbose_name='Электронная почта', null=True)
    phone = models.IntegerField(verbose_name='Номер телефона', null=True)
    address = models.CharField(verbose_name='Адрес доставки', max_length=150, null=True)
    creation_date = models.DateField(verbose_name='Дата создания', null=True, auto_now_add=True)
    update_date = models.DateField(verbose_name='Дата обновления', null=True, auto_now=True)
    balance = models.PositiveIntegerField(verbose_name='Баланс', null=True)
    payment_for_cart = models.PositiveIntegerField(verbose_name='На оплату', default=0)
    status = models.CharField(verbose_name='Статус', max_length=1, choices=STATUS_CHOICES, default='b')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.user}, {self.first_name}, {self.last_name}, ' \
               f'{self.email}, {self.phone}, {self.address}, ' \
               f'{self.creation_date}, {self.balance}'


class PurchasedGoods(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', null=True, on_delete=models.CASCADE)
    good = models.ForeignKey(Goods, verbose_name='Товар', on_delete=models.CASCADE)
    good_quantity = models.PositiveIntegerField(verbose_name='Количество', null=True)
    purchase_date = models.DateField(verbose_name='Дата покупки', null=True, auto_now_add=True)
    purchase_sum = models.IntegerField(verbose_name='Сумма покупки', null=True)

    class Meta:
        verbose_name = 'Приобретенный товар'
        verbose_name_plural = 'Приобретенные товары'

    def __str__(self):
        return f'{self.pk} ,{self.user}, {self.good}, {self.purchase_date}, {self.purchase_sum}'
