# Generated by Django 2.2.7 on 2019-11-22 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_auto_20191122_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='cab_price',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_price',
            field=models.IntegerField(blank=True),
        ),
    ]