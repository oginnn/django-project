# Generated by Django 3.2.18 on 2023-05-29 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20230530_0426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='city',
        ),
    ]
