# Generated by Django 4.2.3 on 2023-07-29 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToyStation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='toy',
            name='description',
            field=models.TextField(default='default'),
        ),
    ]
