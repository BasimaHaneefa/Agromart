# Generated by Django 4.1.7 on 2023-03-27 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0018_market'),
        ('Farmer', '0004_alter_stock_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='farmerRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.farmer')),
            ],
        ),
    ]
