# Generated by Django 3.2.15 on 2022-10-28 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0022_rename_good_obj_purchasedgoods_good'),
        ('app_market_place', '0011_remove_goods_sold'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='sold',
            field=models.ManyToManyField(to='app_users.PurchasedGoods', verbose_name='Куплено'),
        ),
    ]