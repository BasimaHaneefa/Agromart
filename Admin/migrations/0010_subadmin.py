# Generated by Django 4.1.7 on 2023-03-09 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0009_delete_subadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subadmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('photo', models.FileField(upload_to='UserPhoto/')),
                ('password', models.CharField(max_length=50)),
                ('confirmpassword', models.CharField(max_length=50)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.district')),
            ],
        ),
    ]
