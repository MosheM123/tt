# Generated by Django 4.1.7 on 2024-02-28 12:51

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypay', '0005_alter_cart_item_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_cart',
            name='board',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True), size=8),
        ),
    ]
