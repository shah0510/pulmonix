# Generated by Django 3.2.6 on 2023-05-28 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0010_auto_20230522_0518'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Product Code',
                'ordering': ('name',),
            },
        ),
        migrations.AlterModelOptions(
            name='items',
            options={'ordering': ('Patient_name',), 'verbose_name_plural': 'Patients '},
        ),
    ]
