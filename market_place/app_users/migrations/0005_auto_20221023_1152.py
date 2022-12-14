# Generated by Django 3.2.15 on 2022-10-23 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_market_place', '0004_alter_goods_code'),
        ('app_users', '0004_alter_profile_cart'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PurchasedGood',
            new_name='PurchasedGoods',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='cart',
        ),
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.PositiveIntegerField(null=True, verbose_name='Баланс'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
                ('good_quantity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_market_place.goods', verbose_name='Товар')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
