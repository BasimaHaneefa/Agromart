# Generated by Django 4.2 on 2023-04-18 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0020_rename_admin_email_admin_email_and_more'),
        ('User', '0016_sendrequest_payment_sts'),
        ('Farmer', '0015_remove_stock_farmer_product_farmer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='FarmerProducts',
        ),
    ]