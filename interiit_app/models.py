from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import os
from datetime import datetime
from django.utils import timezone
# from uuid import uuid4
# Create your models here.

class CommomChoices:
    iitChoices = (
        ('IITKGP', 'IIT Kharagpur'),
        ('IITB', 'IIT Bombay'),
        ('IITK', 'IIT Kanpur'),
        ('IITM', 'IIT Madras'),
        ('IITD', 'IIT Delhi'),
        ('IITG', 'IIT Guhawati'),
        ('IITR', 'IIT Roorkee'),
        ('IITBBS', 'IIT Bhubaneshwar'),
        ('IITGN', 'IIT Gandhinagar'),
        ('IITH', 'IIT Hyderabad'),
        ('IITJ', 'IIT Jodhpur'),
        ('IITP', 'IIT Patna'),
        ('IITRPR', 'IIT Ropar'),
        ('IITI', 'IIT Indore'),
        ('IITMANDI', 'IIT Mandi'),
        ('IITBHU', 'IIT (BHU) Varanasi'),
        ('IITPKD', 'IIT Palakkad'),
        ('IITTP', 'IIT Tirupati'),
        ('IITISM', 'IIT (ISM) Dhanbad'),
        ('IITBH', 'IIT Bhilai'),
        ('IITGOA', 'IIT Goa'),
        ('IITJM', 'IIT Jammu'),
        ('IITDH', 'IIT Dharwad'),
    )

    binaryChoices = (
        ('YES', 'Yes'),
        ('NO', 'No'),
    )

    foodChoices = (
        ('VEG', 'Vegetarian'),
        ('JAIN', 'Jain'),
        ('NONVEG', 'Non-Vegetarian'),
    )

    genderChoices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
class Sport_Aquatics_Men(models.Model):
    def path_and_rename(instance, filename):
        upload_to = 'AquaticsMeet/Men'
        ext = filename.split('.')[-1]
        namearray = instance.student_name.split(' ')
        namelen = len(namearray)
        name = ''
        for i in range(0, namelen):
            name = name + namearray[i].capitalize()
        filename = '{}_Participant_{}.{}'.format(name, instance.iit_name, ext)
        return os.path.join(upload_to, filename)

    iit_name = models.CharField(max_length=10, choices=CommomChoices.iitChoices)
    student_name = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=15)
    mobile_no = PhoneNumberField()
    email = models.EmailField()
    photo = models.ImageField(upload_to=path_and_rename, null=True, default=None)
    arrival = models.CharField(max_length=20)
    departure = models.CharField(max_length=20)
    timestamp = models.DateTimeField(default=timezone.now, editable=False)
    food = models.CharField(max_length=10, default='VEG', choices=CommomChoices.foodChoices)
    water_polo = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    free_50m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    free_100m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    free_200m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    free_400m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    free_1500m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    back_50m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    back_100m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    back_200m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    breast_50m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    breast_100m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    breast_200m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    b_fly_50m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    b_fly_100m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    i_m_200m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    free_relay_4x100m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    medley_relay_4x100m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)

    def __str__(self):
        return_str = '''
            Name : {}
            Blood Group : {}
            Mobile No. : {}
            Email : {}
        '''.format(
            self.student_name,
            self.blood_group,
            self.mobile_no,
            self.email,
        )
        return return_str

class Sport_Aquatics_Women(models.Model):
    def path_and_rename(instance, filename):
        upload_to = 'AquaticsMeet/Women'
        ext = filename.split('.')[-1]
        namearray = instance.student_name.split(' ')
        namelen = len(namearray)
        name = ''
        for i in range(0, namelen):
            name = name + namearray[i].capitalize()
        filename = '{}_Participant_{}.{}'.format(name, instance.iit_name, ext)
        return os.path.join(upload_to, filename)

    iit_name = models.CharField(max_length=10, choices=CommomChoices.iitChoices)
    student_name = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=15)
    mobile_no = PhoneNumberField()
    email = models.EmailField()
    photo = models.ImageField(upload_to=path_and_rename, null=True, default=None)
    arrival = models.CharField(max_length=20)
    departure = models.CharField(max_length=20)
    timestamp = models.DateTimeField(default=timezone.now, editable=False)
    food = models.CharField(max_length=10, default='VEG', choices=CommomChoices.foodChoices)
    freestyle_50m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    freestyle_100m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    breast_stroke_50m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    back_stroke_50m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    butterfly_50m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    freestyle_relay_4x50m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)

class Sport_Aquatics_Staff(models.Model):
    def path_and_rename(instance, filename):
        upload_to = 'AquaticsMeet/Staff'
        ext = filename.split('.')[-1]
        namearray = instance.staff_name.split(' ')
        namelen = len(namearray)
        name = ''
        for i in range(0, namelen):
            name = name + namearray[i].capitalize()
        filename = '{}_Staff_{}.{}'.format(name, instance.iit_name, ext)
        return os.path.join(upload_to, filename)

    iit_name = models.CharField(max_length=10, choices=CommomChoices.iitChoices)
    staff_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, default='M', choices=CommomChoices.genderChoices)
    blood_group = models.CharField(max_length=15)
    mobile_no = PhoneNumberField()
    email = models.EmailField()
    photo = models.ImageField(upload_to=path_and_rename, null=True, default=None)
    arrival = models.CharField(max_length=20)
    departure = models.CharField(max_length=20)
    timestamp = models.DateTimeField(default=timezone.now, editable=False)
    food = models.CharField(max_length=10, default='VEG', choices=CommomChoices.foodChoices)
    designation = models.CharField(max_length=30)