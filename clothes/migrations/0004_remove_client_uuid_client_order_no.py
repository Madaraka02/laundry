# Generated by Django 4.0.6 on 2022-07-29 21:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0003_remove_client_order_no_client_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='uuid',
        ),
        migrations.AddField(
            model_name='client',
            name='order_no',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
