# Generated by Django 4.2.3 on 2024-02-29 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_order_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deposit',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='rate_percentage',
            field=models.FloatField(blank=True, null=True),
        ),
    ]