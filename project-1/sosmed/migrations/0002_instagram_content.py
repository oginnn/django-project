# Generated by Django 3.2.18 on 2023-05-14 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sosmed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagram',
            name='content',
            field=models.CharField(default='personal', max_length=100),
            preserve_default=False,
        ),
    ]
