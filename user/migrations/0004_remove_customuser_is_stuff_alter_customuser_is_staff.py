# Generated by Django 4.2.3 on 2024-02-28 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_customuser_is_stuff_alter_customuser_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_stuff',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='stuff status'),
        ),
    ]