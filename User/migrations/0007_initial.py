# Generated by Django 4.1.7 on 2023-03-29 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0018_market'),
        ('Farmer', '0011_farmerrequest'),
        ('User', '0006_delete_sendrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('status', models.IntegerField(default=0)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.farmer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Farmer.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.user')),
            ],
        ),
    ]
