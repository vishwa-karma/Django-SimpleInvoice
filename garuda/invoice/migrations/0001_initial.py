# Generated by Django 2.2.7 on 2019-11-22 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=70, unique=True)),
                ('c_adrress', models.TextField()),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Invoicee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_name', models.CharField(max_length=50, unique=True)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('phone_num', models.CharField(max_length=14, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_num', models.CharField(max_length=10, unique=True)),
                ('invoice_date', models.DateField(auto_now=True)),
                ('service', models.CharField(max_length=100, unique=True)),
                ('unt_price', models.IntegerField()),
                ('n_days', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('cab_price', models.IntegerField()),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='invoice.Client', to_field='c_name')),
                ('invoicee_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='invoice.Invoicee', to_field='r_name')),
            ],
        ),
    ]
