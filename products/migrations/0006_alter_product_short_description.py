# Generated by Django 4.0.2 on 2023-03-05 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_short_description_alter_product_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='short description'),
        ),
    ]