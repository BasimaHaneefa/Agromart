# Generated by Django 4.1.7 on 2023-03-27 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0018_market'),
        ('Farmer', '0004_alter_stock_date'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserRequest',
            new_name='SendRequest',
        ),
    ]
