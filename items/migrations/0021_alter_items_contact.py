# Generated by Django 3.2.10 on 2023-06-01 08:28

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0020_remove_product_code_rent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Contact',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]