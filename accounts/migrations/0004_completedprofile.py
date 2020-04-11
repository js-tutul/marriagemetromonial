# Generated by Django 2.2.7 on 2020-04-03 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_delete_completedprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationalID', models.IntegerField(max_length=15)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=20)),
                ('maritalStatus', models.CharField(choices=[('M', 'Married'), ('F', 'Unmarried')], max_length=20)),
                ('Children', models.IntegerField(blank=True, default=0)),
                ('height', models.FloatField(default=0.0)),
                ('bodyType', models.CharField(choices=[('S', 'Slim'), ('F', 'Fat'), ('A', 'Average')], max_length=35)),
                ('Complexion', models.CharField(choices=[('F', 'Fair'), ('VF', 'Very Fair'), ('D', 'Dark'), ('WM', 'Wheatish Medium'), ('WB', 'Wheatish Brown')], max_length=30)),
                ('blodGroup', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('B+', 'B+'), ('B-', 'B-')], max_length=35)),
                ('religon', models.CharField(choices=[('Muslim', 'Muslim'), ('Hindu', 'Hindu'), ('Christian', 'Christian'), ('Buddhist', 'Buddhist'), ('Others', 'Others')], max_length=35)),
                ('mothertongue', models.CharField(choices=[('Bengali', 'Bengali'), ('English', 'English'), ('Others', 'Others')], max_length=35)),
                ('familyvalue', models.CharField(choices=[('Liberal', 'Lineral'), ('Religious', 'Religious'), ('Traditional', 'Traditional'), ('Moderate', 'Moderate')], max_length=35)),
                ('father', models.CharField(choices=[('Retired', 'Retired'), ('Businessman', 'Businessman'), ('Employed', 'Employed'), ('Unemployed', 'Unemployed'), ('Passed Away', 'Passed Away')], max_length=35)),
                ('mother', models.CharField(choices=[('Home Maker', 'Home Maker'), ('Retired', 'Retired'), ('Businessman', 'Businessman'), ('Employed', 'Employed'), ('Unemployed', 'Unemployed'), ('Passed Away', 'Passed Away')], max_length=35)),
                ('sister', models.IntegerField(default=0)),
                ('brother', models.IntegerField(default=0)),
                ('education', models.CharField(choices=[('Phd/Doctorate', 'Phd/Doctorate'), ('Master', 'Master'), ('MBA', 'MBA'), ('Diploma', 'Diploma'), ('HSC', 'HSC'), ('SSC', 'SSC'), ('Alim', 'Alim'), ('Dakhil', 'Dakhil'), ('Fajil', 'Fajil'), ('Kamil', 'Kamil')], max_length=50)),
                ('universitycollege', models.CharField(default='Null', max_length=100)),
                ('profession', models.CharField(default='Null', max_length=100)),
                ('designation', models.CharField(default='Null', max_length=100)),
                ('currentlivingcourtry', models.CharField(max_length=100)),
                ('currentlivingcity', models.CharField(max_length=100)),
                ('currentlivingarea', models.CharField(max_length=100)),
                ('residentialstatus', models.CharField(choices=[('Rented', 'Rented'), ('Owner', 'Owner')], max_length=35)),
                ('homecountry', models.CharField(max_length=100)),
                ('homedistrict', models.CharField(max_length=100)),
                ('aboutyou', models.TextField(max_length=300)),
                ('aboutfamily', models.TextField(max_length=300)),
                ('preferredage', models.CharField(choices=[('18-25', '18-25'), ('26-30', '26-30'), ('30-35', '30-35'), ('36-40', '36-40'), ('40-50', '40-50'), ('50+', '50+')], max_length=35)),
                ('preferredmarrige', models.CharField(choices=[('Married', 'Married'), ('Unmarried', 'Unmarried'), ('Divorced', 'Divorced'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed'), ('Separated', 'Separated'), ('No Matter', 'No Matter')], max_length=35)),
                ('patnerreligon', models.CharField(choices=[('Muslim', 'Muslim'), ('Hindu', 'Hindu'), ('Christian', 'Christian'), ('Buddhist', 'Buddhist'), ('Others', 'Others')], max_length=35)),
                ('patnerhomecountry', models.CharField(max_length=30)),
                ('patnercurrentliving', models.CharField(max_length=30)),
                ('patnereducation', models.CharField(choices=[('Phd/Doctorate', 'Phd/Doctorate'), ('Master', 'Master'), ('MBA', 'MBA'), ('Diploma', 'Diploma'), ('HSC', 'HSC'), ('SSC', 'SSC'), ('Alim', 'Alim'), ('Dakhil', 'Dakhil'), ('Fajil', 'Fajil'), ('Kamil', 'Kamil')], max_length=50)),
                ('patnerprofession', models.CharField(max_length=50)),
                ('aboutpatner', models.TextField(max_length=300)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
