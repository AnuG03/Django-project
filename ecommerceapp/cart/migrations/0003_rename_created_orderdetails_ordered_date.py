# Generated by Django 5.1.2 on 2024-11-16 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_payment_orderdetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetails',
            old_name='created',
            new_name='ordered_date',
        ),
    ]