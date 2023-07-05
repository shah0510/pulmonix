# Generated by Django 3.2.6 on 2023-07-02 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0022_alter_items_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='Issue_date',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='items',
            old_name='Vendor',
            new_name='Supplied_by',
        ),
        migrations.RemoveField(
            model_name='items',
            name='Product_name',
        ),
        migrations.RemoveField(
            model_name='items',
            name='Rent_end_date',
        ),
        migrations.RemoveField(
            model_name='items',
            name='Rent_start_date',
        ),
        migrations.RemoveField(
            model_name='items',
            name='Technician',
        ),
    ]