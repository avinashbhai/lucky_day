# Generated by Django 2.0.2 on 2019-04-20 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lucky_dayapp', '0005_auto_20190419_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_no',
        ),
    ]
