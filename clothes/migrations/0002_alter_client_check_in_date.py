# Generated by Django 4.0.6 on 2022-07-25 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='check_in_date',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
