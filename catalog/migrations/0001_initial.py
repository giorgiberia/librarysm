# Generated by Django 3.1 on 2020-08-07 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('status', models.IntegerField()),
                ('takenBy', models.CharField(max_length=255)),
            ],
        ),
    ]
