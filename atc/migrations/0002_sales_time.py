# Generated by Django 4.2.4 on 2024-06-22 17:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]