# Generated by Django 4.2.14 on 2024-07-18 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_rename_discount_product_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartMent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.TextField(default='UNKNOWN')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
    ]