from django.contrib.auth.models import User
from django.db import models


GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
MARITAL_CHOICES = (
        ('M', 'Married'),
        ('F', 'Unmarried')
    )
BODY_CHOICES = (
        ('S', 'Slim'),
        ('F', 'Fat'),
        ('A','Average')
    )
COM_CHOICES = (
        ('F', 'Fair'),
        ('VF', 'Very Fair'),
        ('D','Dark'),
        ('WM','Wheatish Medium'),
        ('WB','Wheatish Brown')
    )
BLOOD_CHOICES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('O+','O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('B+', 'B+'),
        ('B-', 'B-')
    )
RELIGON_CHOICES = (
        ('Muslim', 'Muslim'),
        ('Hindu', 'Hindu'),
        ('Christian','Christian'),
        ('Buddhist', 'Buddhist'),
        ('Others', 'Others')
    )
PATNER_RELIGON_CHOICES = (
        ('Muslim', 'Muslim'),
        ('Hindu', 'Hindu'),
        ('Christian','Christian'),
        ('Buddhist', 'Buddhist'),
        ('Others', 'Others')
    )
MOTHER_TONGUE_CHOICES = (
        ('Bengali', 'Bengali'),
        ('English', 'English'),
        ('Others', 'Others')
    )
FAMILY_VALUE=(
    ('Liberal','Lineral'),
    ('Religious','Religious'),
    ('Traditional','Traditional'),
    ('Moderate','Moderate'),

)
FATHER_VALUE=(
    ('Retired','Retired'),
    ('Businessman','Businessman'),
    ('Employed','Employed'),
    ('Unemployed','Unemployed'),
    ('Passed Away','Passed Away')

)
MOTHER_VALUE=(
    ('Home Maker','Home Maker'),
    ('Retired','Retired'),
    ('Businessman','Businessman'),
    ('Employed','Employed'),
    ('Unemployed','Unemployed'),
    ('Passed Away','Passed Away')

)
EDUCATION=(
    ('Phd/Doctorate','Phd/Doctorate'),
    ('Master','Master'),
    ('MBA','MBA'),
    ('Diploma','Diploma'),
    ('HSC','HSC'),
    ('SSC','SSC'),
    ('Alim','Alim'),
    ('Dakhil','Dakhil'),
    ('Fajil','Fajil'),
    ('Kamil','Kamil')

)
PATNEREDUCATION=(
    ('Phd/Doctorate','Phd/Doctorate'),
    ('Master','Master'),
    ('MBA','MBA'),
    ('Diploma','Diploma'),
    ('HSC','HSC'),
    ('SSC','SSC'),
    ('Alim','Alim'),
    ('Dakhil','Dakhil'),
    ('Fajil','Fajil'),
    ('Kamil','Kamil')

)
RESIDENTIAL=(
    ('Rented','Rented'),
    ('Owner','Owner')
)
PREFEREDMARRIAGE=(
    ('Married','Married'),
    ('Unmarried','Unmarried'),
    ('Divorced','Divorced'),
    ('Divorced','Divorced'),
    ('Widowed','Widowed'),
    ('Separated','Separated'),
    ('No Matter','No Matter')
)
AGE=(
    ('18-25','18-25'),
    ('26-30','26-30'),
    ('30-35','30-35'),
    ('36-40','36-40'),
    ('40-50','40-50'),
    ('50+','50+'),


)
# class CompletedProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.PROTECT, default=None)
#     nationalID=models.IntegerField(max_length=15,blank=False)
#     gender = models.CharField(choices=GENDER_CHOICES, max_length=20)
#     phone=models.IntegerField(blank=False,max_length=11)
#     city=models.CharField(max_length=50,blank=False)
#     birth=models.DateTimeField(auto_now=False,auto_now_add=True,blank=False)
#     maritalStatus = models.CharField(choices=MARITAL_CHOICES, max_length=20)
#     Children=models.IntegerField(blank=False,default=0)
#     height=models.FloatField(blank=False,default=0.0)
#     bodyType=models.CharField(choices=BODY_CHOICES,max_length=35,blank=False)
#     Complexion=models.CharField(choices=COM_CHOICES,max_length=30,blank=False)
#     blodGroup=models.CharField(choices=BLOOD_CHOICES,max_length=35,blank=False)
#     religon=models.CharField(choices=RELIGON_CHOICES,max_length=35,blank=False)
#     mothertongue=models.CharField(choices=MOTHER_TONGUE_CHOICES,max_length=35,blank=False)
#     familyvalue=models.CharField(choices=FAMILY_VALUE,max_length=35,blank=False)
#     father=models.CharField(choices=FATHER_VALUE,max_length=35,blank=False)
#     mother=models.CharField(choices=MOTHER_VALUE,max_length=35,blank=False)
#     sister=models.IntegerField(blank=False,default=0)
#     brother=models.IntegerField(blank=False,default=0)
#     education = models.CharField(choices=EDUCATION, max_length=50, blank=False)
#     universitycollege=models.CharField(max_length=100,blank=False,default="Null")
#     profession=models.CharField(max_length=100,blank=False,default="Null")
#     designation=models.CharField(max_length=100,blank=False,default="Null")
#     currentlivingcourtry=models.CharField(max_length=100,blank=False)
#     currentlivingcity=models.CharField(max_length=100,blank=False)
#     currentlivingarea=models.CharField(max_length=100,blank=False)
#     residentialstatus = models.CharField(choices=RESIDENTIAL, max_length=35, blank=False)
#     homecountry = models.CharField(max_length=100, blank=False)
#     homedistrict = models.CharField(max_length=100, blank=False)
#     aboutyou=models.TextField(max_length=300,blank=False)
#     aboutfamily=models.TextField(max_length=300,blank=False)
#     preferredage=models.CharField(choices=AGE, max_length=35, blank=False)
#     preferredmarrige=models.CharField(choices=PREFEREDMARRIAGE, max_length=35, blank=False)
#     patnerreligon=models.CharField(choices=PATNER_RELIGON_CHOICES,max_length=35,blank=False)
#     patnerhomecountry=models.CharField(max_length=30,blank=False)
#     patnercurrentliving=models.CharField(max_length=30,blank=False)
#     patnereducation=models.CharField(choices=PATNEREDUCATION, max_length=50, blank=False)
#     patnerprofession = models.CharField(max_length=50, blank=False)
#     aboutpatner = models.TextField(max_length=300, blank=False)
#
#     def __str__(self):
#         return str(self.user)

class CompletedRegister(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, default=None)
    nationalID=models.IntegerField(blank=False)
    gender = models.CharField(max_length=20,blank=False)
    phone=models.IntegerField(blank=False)
    birth=models.CharField(max_length=20,blank=False)
    maritalStatus = models.CharField(max_length=30,blank=False)
    Children=models.IntegerField(blank=False,default=0)
    height=models.FloatField(blank=False,default=0.0)
    bodyType=models.CharField(max_length=35,blank=False)
    Complexion=models.CharField(max_length=30,blank=False)
    blodGroup=models.CharField(max_length=35,blank=False)
    religon=models.CharField(max_length=35,blank=False)
    mothertongue=models.CharField(max_length=35,blank=False)
    familyvalue=models.CharField(max_length=35,blank=False)
    father=models.CharField(max_length=35,blank=False)
    mother=models.CharField(max_length=35,blank=False)
    sister=models.IntegerField(blank=False,default=0)
    brother=models.IntegerField(blank=False,default=0)
    education = models.CharField(max_length=50, blank=False)
    universitycollege=models.CharField(max_length=100,blank=False,default="Null")
    profession=models.CharField(max_length=100,blank=False,default="Null")
    designation=models.CharField(max_length=100,blank=False,default="Null")
    currentlivingcourtry=models.CharField(max_length=100,blank=False)
    currentlivingcity=models.CharField(max_length=100,blank=False)
    currentlivingarea=models.CharField(max_length=100,blank=False)
    residentialstatus = models.CharField(max_length=35, blank=False)
    homecountry = models.CharField(max_length=100, blank=False)
    homedistrict = models.CharField(max_length=100, blank=False)
    aboutyou=models.TextField(max_length=300,blank=False)
    aboutfamily=models.TextField(max_length=300,blank=False)
    preferredage=models.CharField(max_length=35, blank=False)
    preferredmarrige=models.CharField(max_length=35, blank=False)
    patnerreligon=models.CharField(max_length=35,blank=False)
    patnerhomecountry=models.CharField(max_length=30,blank=False)
    patnercurrentliving=models.CharField(max_length=30,blank=False)
    patnereducation=models.CharField(max_length=50, blank=False)
    patnerprofession = models.CharField(max_length=50, blank=False)
    aboutpatner = models.TextField(max_length=300, blank=False)
    website = models.URLField(default='http://www.facebook.com/')
    thumb = models.ImageField(upload_to='profile_image', blank=False, default='default.jpg',)

    def __str__(self):
        return str(self.user)