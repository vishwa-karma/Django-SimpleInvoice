# Generated by Django 2.2.7 on 2019-11-22 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0007_auto_20191122_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='cab_price',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_date',
            field=models.DateField(),
        ),
    ]
