from django.contrib.auth.models import User
from django.db import models


class Store(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100, null=True)
    description = models.TextField(verbose_name='Описание', max_length=1500, null=True)
    owner = models.ForeignKey(User, verbose_name='Владелец', null=True, on_delete=models.CASCADE)
    creation_date = models.DateField(verbose_name='Дата создания', null=True, auto_now_add=True)
    update_date = models.DateField(verbose_name='Дата обновления', null=True, auto_now=True)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return f'{self.title}, {self.owner}, {self.creation_date}'


class Goods(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=100, null=True)
    description = models.TextField(verbose_name='Описание', max_length=1500, null=True)
    creation_date = models.DateField(verbose_name='Дата создание', null=True, auto_now_add=True)
    update_date = models.DateField(verbose_name='Дата обновления', null=True, auto_now=True)
    store = models.ForeignKey(Store, verbose_name='Магазин', null=True, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(verbose_name='Цена', null=True)
    code = models.IntegerField(verbose_name='Артикул', null=True)
    remaining_stock = models.PositiveIntegerField(verbose_name='Остаток', null=True)
    purchases = models.ManyToManyField('app_users.PurchasedGoods', verbose_name='Куплено', blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.title}, {self.store}, {self.purchases}'


class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', null=True, on_delete=models.CASCADE)
    good = models.ForeignKey(Goods, verbose_name='Товар', on_delete=models.CASCADE)
    add_datetime = models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)
    good_quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)
    ordered_good_price_sum = models.IntegerField(verbose_name='Цена товара', null=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'{self.user}, {self.good}, {self.add_datetime}, {self.good_quantity}'
