# Generated by Django 4.1.7 on 2023-03-29 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0030_feedback_complaint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='date',
        ),
    ]
