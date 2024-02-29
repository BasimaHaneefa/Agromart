# Generated by Django 4.1.7 on 2023-03-10 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0003_initial'),
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
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('logo', models.CharField(max_length=50)),
                ('proof', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('confirmpassword', models.CharField(max_length=50)),
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
    ]
