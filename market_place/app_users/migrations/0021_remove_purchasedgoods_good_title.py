# Generated by Django 3.2.15 on 2022-10-28 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0020_alter_purchasedgoods_good_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasedgoods',
            name='good_title',
        ),
    ]
