# Generated by Django 2.2.7 on 2020-04-06 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20200405_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='completedregister',
            name='thumb',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_image'),
        ),
        migrations.AddField(
            model_name='completedregister',
            name='website',
            field=models.URLField(default='http://www.facebook.com/'),
        ),
        migrations.DeleteModel(
            name='Userprofile',
        ),
    ]