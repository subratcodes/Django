# Generated by Django 4.2.14 on 2024-07-18 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_remove_product_name_product_content_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.TextField(blank=True, default='Some text'),
        ),
    ]
