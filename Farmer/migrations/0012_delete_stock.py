# Generated by Django 4.1.7 on 2023-03-30 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Farmer', '0011_farmerrequest'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Stock',
        ),
    ]