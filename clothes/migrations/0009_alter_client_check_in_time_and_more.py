# Generated by Django 4.0.6 on 2022-07-25 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0008_alter_client_check_in_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='check_in_time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='check_out_time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]