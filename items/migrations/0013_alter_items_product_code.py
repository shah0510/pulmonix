# Generated by Django 3.2.6 on 2023-05-28 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0012_product_code_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Product_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='items.product_code'),
        ),
    ]
