# Generated by Django 5.1.4 on 2024-12-30 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0008_customer_cart_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cart_items',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
