# Generated by Django 4.2 on 2023-04-14 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0031_remove_complaint_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producttype_name', models.CharField(max_length=50)),
            ],
        ),
    ]
