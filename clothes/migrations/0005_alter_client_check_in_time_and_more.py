# Generated by Django 4.0.6 on 2022-07-25 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0004_remove_client_clothes_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='check_in_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='check_out_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]