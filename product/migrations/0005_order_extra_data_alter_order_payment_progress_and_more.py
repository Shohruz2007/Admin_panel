# Generated by Django 4.2.3 on 2024-03-04 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_paymentmethod_rename_deposit_order_balance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='extra_data',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_progress',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='payment_period',
            field=models.IntegerField(verbose_name='Length of payment period in months'),
        ),
    ]
