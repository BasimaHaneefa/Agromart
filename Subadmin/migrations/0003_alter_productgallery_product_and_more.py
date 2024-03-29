# Generated by Django 4.2 on 2023-04-18 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0034_alter_subadmin_district'),
        ('Subadmin', '0002_rename_product_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productgallery',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Subadmin.products'),
        ),
        migrations.AlterField(
            model_name='products',
            name='producttype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.producttype'),
        ),
        migrations.AlterField(
            model_name='products',
            name='subadmin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.subadmin'),
        ),
        migrations.AlterField(
            model_name='productstock',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Subadmin.products'),
        ),
    ]
