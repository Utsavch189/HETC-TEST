# Generated by Django 3.2.8 on 2022-05-26 09:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0012_auto_20220526_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 14, 44, 22, 439370)),
        ),
    ]
