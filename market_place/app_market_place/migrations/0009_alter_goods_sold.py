# Generated by Django 3.2.15 on 2022-10-27 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0015_purchasedgoods'),
        ('app_market_place', '0008_goods_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='sold',
            field=models.ManyToManyField(null=True, to='app_users.PurchasedGoods', verbose_name='Куплена'),
        ),
    ]