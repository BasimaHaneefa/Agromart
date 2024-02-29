# Generated by Django 4.2 on 2023-04-20 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0021_alter_farmer_place_alter_market_place_and_more'),
        ('Market', '0001_initial'),
        ('Farmer', '0018_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionSlotBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slotbookdate', models.DateField()),
                ('slotbooktime', models.TimeField()),
                ('farmer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.farmer')),
                ('marketevent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Market.marketevent')),
            ],
        ),
        migrations.CreateModel(
            name='SlotReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slotreply_no', models.CharField(max_length=50)),
                ('slotreply_allocatetime', models.CharField(max_length=50)),
                ('slotbook', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Farmer.auctionslotbooking')),
            ],
        ),
    ]