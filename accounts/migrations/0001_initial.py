# Generated by Django 2.2.7 on 2020-04-03 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='Description of Author', max_length=1000)),
                ('city', models.CharField(default='City name', max_length=20)),
                ('website', models.URLField(default='http://www.facebook.com/')),
                ('phone', models.IntegerField(default=0)),
                ('thumb', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_image')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
