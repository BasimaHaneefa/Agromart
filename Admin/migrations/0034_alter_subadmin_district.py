# Generated by Django 4.2 on 2023-04-18 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0033_alter_subadmin_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subadmin',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.district'),
        ),
    ]