# Generated by Django 5.0.7 on 2025-04-03 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paymnt', '0002_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='transaction_id',
        ),
    ]
