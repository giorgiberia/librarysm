# Generated by Django 3.1 on 2020-08-08 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20200808_2354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='returned_at',
        ),
    ]
