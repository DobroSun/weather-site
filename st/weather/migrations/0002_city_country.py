# Generated by Django 2.2 on 2019-07-12 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
