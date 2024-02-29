# Generated by Django 4.2 on 2023-04-18 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0021_alter_farmer_place_alter_market_place_and_more'),
        ('Subadmin', '0003_alter_productgallery_product_and_more'),
        ('Farmer', '0017_alter_farmerproducts_ptype_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=50)),
                ('req_date', models.DateField(auto_now=True)),
                ('total_amnt', models.CharField(max_length=50)),
                ('req_sts', models.IntegerField(default=0)),
                ('p_sts', models.IntegerField(default=0)),
                ('farmer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.farmer')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Subadmin.products')),
            ],
        ),
    ]
