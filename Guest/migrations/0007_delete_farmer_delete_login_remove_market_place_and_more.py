# Generated by Django 4.1.7 on 2023-03-10 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0006_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Farmer',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.RemoveField(
            model_name='market',
            name='place',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Market',
        ),
    ]
