# Generated by Django 2.2.7 on 2020-04-05 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20200405_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completedregister',
            name='city',
        ),
    ]
