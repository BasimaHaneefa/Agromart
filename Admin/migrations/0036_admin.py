# Generated by Django 4.2.7 on 2024-02-10 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0035_rename_producttype_sproducttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
