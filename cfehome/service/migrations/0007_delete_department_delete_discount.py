# Generated by Django 4.2.14 on 2024-07-19 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_department_remove_product_discount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DepartMent',
        ),
        migrations.DeleteModel(
            name='Discount',
        ),
    ]
