# Generated by Django 4.2.6 on 2024-01-12 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_reportingresult_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportingresult',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos'),
        ),
    ]
