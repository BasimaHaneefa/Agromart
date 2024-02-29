# Generated by Django 4.2 on 2023-04-26 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0021_alter_farmer_place_alter_market_place_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='password',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='password',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
