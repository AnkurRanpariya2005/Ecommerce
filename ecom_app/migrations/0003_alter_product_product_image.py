# Generated by Django 4.2.4 on 2023-08-10 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0002_product_product_category_product_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='', upload_to='ecom_app/static/product/images'),
        ),
    ]