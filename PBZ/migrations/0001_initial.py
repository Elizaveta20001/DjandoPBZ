# Generated by Django 3.1.1 on 2020-10-13 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('passport_id', models.IntegerField()),
                ('passport_series', models.CharField(max_length=2)),
                ('bank_details', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('region_name', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('house_number', models.IntegerField()),
                ('flat_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Waybill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_price', models.FloatField()),
                ('date', models.DateField()),
                ('number_of_product', models.IntegerField()),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='PBZ.customer')),
                ('destination', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='PBZ.destination')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='PBZ.product')),
            ],
        ),
    ]
