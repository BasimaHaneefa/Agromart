# Generated by Django 4.1.7 on 2023-03-29 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0019_marketfeedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfeedback',
            name='farmer',
        ),
        migrations.RemoveField(
            model_name='userfeedback',
            name='market',
        ),
        migrations.RemoveField(
            model_name='userfeedback',
            name='user',
        ),
        migrations.DeleteModel(
            name='marketFeedback',
        ),
        migrations.DeleteModel(
            name='UserFeedback',
        ),
    ]