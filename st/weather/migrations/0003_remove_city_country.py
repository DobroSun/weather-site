# Generated by Django 2.2 on 2019-07-14 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_city_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='country',
        ),
    ]