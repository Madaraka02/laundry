# Generated by Django 4.0.6 on 2022-07-30 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='pricce',
            new_name='price',
        ),
    ]
