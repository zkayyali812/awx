# Generated by Django 4.2.6 on 2024-01-16 17:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0190_instance_receptor_installation_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receptoraddress',
            name='canonical',
            field=models.BooleanField(default=False, help_text='If True, this address is the canonical address for the instance.'),
        ),
    ]