# Generated by Django 5.0.2 on 2024-02-25 12:52

import picklefield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easypay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_cart',
            name='board2',
            field=picklefield.fields.PickledObjectField(editable=False),
        ),
    ]
