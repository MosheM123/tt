# Generated by Django 5.0.2 on 2024-02-26 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypay', '0004_cart_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_item',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
