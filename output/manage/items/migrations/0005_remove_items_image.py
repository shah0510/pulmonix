# Generated by Django 3.2.6 on 2023-04-30 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20230430_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='image',
        ),
    ]
