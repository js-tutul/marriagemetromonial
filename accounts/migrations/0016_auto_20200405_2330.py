# Generated by Django 2.2.7 on 2020-04-05 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_remove_completedregister_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedregister',
            name='preferredage',
            field=models.CharField(max_length=35),
        ),
    ]
