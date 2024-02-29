# Generated by Django 4.2 on 2023-04-18 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0034_alter_subadmin_district'),
        ('Guest', '0020_rename_admin_email_admin_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.place'),
        ),
        migrations.AlterField(
            model_name='market',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.place'),
        ),
        migrations.AlterField(
            model_name='subadmin',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.place'),
        ),
        migrations.AlterField(
            model_name='user',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.place'),
        ),
    ]
