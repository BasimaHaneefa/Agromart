# Generated by Django 4.1.7 on 2023-03-10 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0010_subadmin'),
        ('Guest', '0007_delete_farmer_delete_login_remove_market_place_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('logo', models.CharField(max_length=50)),
                ('proof', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('confirmpassword', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('logo', models.CharField(max_length=50)),
                ('proof', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('confirmpassword', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('logo', models.FileField(max_length=50, upload_to='')),
                ('proof', models.FileField(max_length=50, upload_to='')),
                ('password', models.CharField(max_length=50)),
                ('confirmpassword', models.CharField(max_length=50)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.place')),
            ],
        ),
    ]
