# Generated by Django 2.2.7 on 2020-04-03 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200403_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedprofile',
            name='Children',
            field=models.IntegerField(default=0),
        ),
    ]
