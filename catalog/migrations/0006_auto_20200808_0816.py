# Generated by Django 3.1 on 2020-08-08 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20200808_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='returned_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='taken_at',
            field=models.DateTimeField(null=True),
        ),
    ]
