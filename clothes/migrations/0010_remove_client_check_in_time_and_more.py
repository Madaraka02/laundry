# Generated by Django 4.0.6 on 2022-07-25 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0009_alter_client_check_in_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='check_in_time',
        ),
        migrations.RemoveField(
            model_name='client',
            name='check_out_time',
        ),
        migrations.AlterField(
            model_name='client',
            name='check_in_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='check_out_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
