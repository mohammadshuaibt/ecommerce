# Generated by Django 5.1.4 on 2024-12-31 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecommerce_app', '0011_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Pending', max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.product')),
            ],
        ),
    ]
