# Generated by Django 4.2 on 2023-04-20 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farmer', '0020_auctionslotbooking_slot_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionslotbooking',
            name='slotbookdate',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='auctionslotbooking',
            name='slotbooktime',
            field=models.TimeField(auto_now=True),
        ),
    ]
