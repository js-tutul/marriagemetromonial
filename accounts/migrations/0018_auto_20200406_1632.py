# Generated by Django 2.2.7 on 2020-04-06 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20200406_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedregister',
            name='nationalID',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='completedregister',
            name='phone',
            field=models.IntegerField(),
        ),
    ]