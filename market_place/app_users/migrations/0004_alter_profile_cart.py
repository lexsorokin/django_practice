# Generated by Django 3.2.15 on 2022-10-23 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_market_place', '0004_alter_goods_code'),
        ('app_users', '0003_profile_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cart',
            field=models.ManyToManyField(blank=True, null=True, to='app_market_place.Goods', verbose_name='Корзина'),
        ),
    ]
