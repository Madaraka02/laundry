# Generated by Django 4.0.6 on 2022-07-25 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0011_alter_client_check_out_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='check_out_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
