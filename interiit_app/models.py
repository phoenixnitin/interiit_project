from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import os
from datetime import datetime
from django.utils import timezone
# from uuid import uuid4
# Create your models here.

class CommomChoices:
    iitChoices = (
        ('IIT KHARAGPUR', 'IIT Kharagpur'),
        ('IIT BOMBAY', 'IIT Bombay'),
        ('IIT KANPUR', 'IIT Kanpur'),
        ('IIT MADRAS', 'IIT Madras'),
        ('IIT DELHI', 'IIT Delhi'),
        ('IIT GUWAHATI', 'IIT Guwahati'),
        ('IIT ROORKEE', 'IIT Roorkee'),
        ('IIT BHUBANESHWAR', 'IIT Bhubaneshwar'),
        ('IIT GANDHINAGAR', 'IIT Gandhinagar'),
        ('IIT HYDERABAD', 'IIT Hyderabad'),
        ('IIT JODHPUR', 'IIT Jodhpur'),
        ('IIT PATNA', 'IIT Patna'),
        ('IIT ROPAR', 'IIT Ropar'),
        ('IIT INDORE', 'IIT Indore'),
        ('IIT MANDI', 'IIT Mandi'),
        ('IIT (BHU) VARANASI', 'IIT (BHU) Varanasi'),
        ('IIT PALAKKAD', 'IIT Palakkad'),
        ('IIT TIRUPATI', 'IIT Tirupati'),
        ('IIT (ISM) DHANBAD', 'IIT (ISM) Dhanbad'),
        ('IIT BHILAI', 'IIT Bhilai'),
        ('IIT GOA', 'IIT Goa'),
        ('IIT JAMMU', 'IIT Jammu'),
        ('IIT DHARWAD', 'IIT Dharwad'),
    )

    binaryChoices = (
        ('YES', 'Yes'),
        ('NO', 'No'),
        ('RESERVE', 'Reserve'),
    )

    foodChoices = (
        ('VEGETARIAN', 'Vegetarian'),
        ('JAIN', 'Jain'),
        ('NON-VEGETARIAN', 'Non-Vegetarian'),
    )

    genderChoices = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )

    bloodGroupChoices = (
        ('O-', 'O-'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('A+', 'A+'),
        ('B-', 'B-'),
        ('B+', 'B+'),
        ('AB-', 'AB-'),
        ('AB+', 'AB+'),
    )

    transportChoices = (
        ('Flight', 'Flight'),
        ('Train', 'Train'),
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

    iit_name = models.CharField(max_length=25, choices=CommomChoices.iitChoices)
    student_name = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=5, choices=CommomChoices.bloodGroupChoices)
    mobile_no = PhoneNumberField()
    email = models.EmailField()
    photo = models.ImageField(upload_to=path_and_rename, null=True, default=None)
    mode_of_transportation = models.CharField(max_length=10, choices=CommomChoices.transportChoices, blank=True, null=True)
    transport_name = models.CharField(max_length=50, blank=True, null=True)
    arrival_date = models.CharField(max_length=20, blank=True, null=True)
    arrival_time = models.CharField(max_length=20, blank=True, null=True)
    departure_date = models.CharField(max_length=20, blank=True, null=True)
    departure_time = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now, editable=False)
    food = models.CharField(max_length=20, default='VEGETARIAN', choices=CommomChoices.foodChoices)
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

    iit_name = models.CharField(max_length=25, choices=CommomChoices.iitChoices)
    student_name = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=5, choices=CommomChoices.bloodGroupChoices)
    mobile_no = PhoneNumberField()
    email = models.EmailField()
    photo = models.ImageField(upload_to=path_and_rename, null=True, default=None)
    mode_of_transportation = models.CharField(max_length=10, choices=CommomChoices.transportChoices, blank=True, null=True)
    transport_name = models.CharField(max_length=50, blank=True, null=True)
    arrival_date = models.CharField(max_length=20, blank=True, null=True)
    arrival_time = models.CharField(max_length=20, blank=True, null=True)
    departure_date = models.CharField(max_length=20, blank=True, null=True)
    departure_time = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now, editable=False)
    food = models.CharField(max_length=20, default='VEGETARIAN', choices=CommomChoices.foodChoices)
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

    iit_name = models.CharField(max_length=25, choices=CommomChoices.iitChoices)
    staff_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=8, default='MALE', choices=CommomChoices.genderChoices)
    blood_group = models.CharField(max_length=5, choices=CommomChoices.bloodGroupChoices)
    mobile_no = PhoneNumberField()
    email = models.EmailField()
    photo = models.ImageField(upload_to=path_and_rename, null=True, default=None)
    mode_of_transportation = models.CharField(max_length=10, choices=CommomChoices.transportChoices, blank=True, null=True)
    transport_name = models.CharField(max_length=50, blank=True, null=True)
    arrival_date = models.CharField(max_length=20, blank=True, null=True)
    arrival_time = models.CharField(max_length=20, blank=True, null=True)
    departure_date = models.CharField(max_length=20, blank=True, null=True)
    departure_time = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now, editable=False)
    food = models.CharField(max_length=20, default='VEGETARIAN', choices=CommomChoices.foodChoices)
    designation = models.CharField(max_length=30)

class Sport_Athletics_Men(models.Model):
    def path_and_rename(instance, filename):
        upload_to = 'MainMeet/{}/Men/Athletics'.format(instance.iit_name)
        ext = filename.split('.')[-1]
        namearray = instance.student_name.split(' ')
        namelen = len(namearray)
        name = ''
        for i in range(0, namelen):
            name = name + namearray[i].capitalize()
        filename = '{}_Participant_Athletics_{}.{}'.format(name, instance.iit_name, ext)
        return os.path.join(upload_to, filename)

    iit_name = models.CharField(max_length=25, choices=CommomChoices.iitChoices)
    student_name = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=5, choices=CommomChoices.bloodGroupChoices)
    mobile_no = PhoneNumberField()
    email = models.EmailField()
    food = models.CharField(max_length=20, default='VEGETARIAN', choices=CommomChoices.foodChoices)
    photo = models.ImageField(upload_to=path_and_rename, null=True, default=None)
    _100m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    _200m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    _400m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    _800m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    _1500m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    _5000m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    hurdles_110m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    hurdles_400m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    high_jump = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    long_jump = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    triple_jump = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    pole_vault = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    shot_put = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    discuss_throw = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    javelin_throw = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    hammer_throw = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    relay_4x100m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    relay_4x400m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)

class Sport_Athletics_Women(models.Model):
    def path_and_rename(instance, filename):
        upload_to = 'MainMeet/{}/Women/Athletics'.format(instance.iit_name)
        ext = filename.split('.')[-1]
        namearray = instance.student_name.split(' ')
        namelen = len(namearray)
        name = ''
        for i in range(0, namelen):
            name = name + namearray[i].capitalize()
        filename = '{}_Participant_Athletics_{}.{}'.format(name, instance.iit_name, ext)
        return os.path.join(upload_to, filename)

    iit_name = models.CharField(max_length=25, choices=CommomChoices.iitChoices)
    student_name = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=5, choices=CommomChoices.bloodGroupChoices)
    mobile_no = PhoneNumberField()
    email = models.EmailField()
    food = models.CharField(max_length=20, default='VEGETARIAN', choices=CommomChoices.foodChoices)
    photo = models.ImageField(upload_to=path_and_rename, null=True, default=None)
    _100m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    _200m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    _400m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    _800m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    _1500m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    high_jump = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    long_jump = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    shot_put = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    discuss_throw = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    relay_4x100m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    relay_4x400m = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)

class Staff(models.Model):
    def path_and_rename(instance, filename):
        upload_to = 'MainMeet/{}/FacultyAndStaff/{}'.format(instance.iit_name, instance.sport_name)
        ext = filename.split('.')[-1]
        namearray = instance.staff_name.split(' ')
        namelen = len(namearray)
        name = ''
        for i in range(0, namelen):
            name = name + namearray[i].capitalize()
        filename = '{}_Staff_{}_{}.{}'.format(name, instance.sport_name, instance.iit_name, ext)
        return os.path.join(upload_to, filename)

    sport_name = models.CharField(max_length=30, null=True, blank=True)
    iit_name = models.CharField(max_length=25, choices=CommomChoices.iitChoices)
    staff_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=8, default='MALE', choices=CommomChoices.genderChoices)
    blood_group = models.CharField(max_length=5, choices=CommomChoices.bloodGroupChoices)
    mobile_no = PhoneNumberField()
    email = models.EmailField()
    food = models.CharField(max_length=20, default='VEGETARIAN', choices=CommomChoices.foodChoices)
    designation = models.CharField(max_length=30)
    photo = models.ImageField(upload_to=path_and_rename, null=True, default=None)

class Sport_Weightlifting(models.Model):
    def path_and_rename(instance, filename):
        upload_to = 'MainMeet/{}/Men/Weightlifting'.format(instance.iit_name)
        ext = filename.split('.')[-1]
        namearray = instance.student_name.split(' ')
        namelen = len(namearray)
        name = ''
        for i in range(0, namelen):
            name = name + namearray[i].capitalize()
        filename = '{}_Participant_Weightlifting_{}.{}'.format(name, instance.iit_name, ext)
        return os.path.join(upload_to, filename)

    iit_name = models.CharField(max_length=25, choices=CommomChoices.iitChoices)
    student_name = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=5, choices=CommomChoices.bloodGroupChoices)
    mobile_no = PhoneNumberField()
    email = models.EmailField()
    food = models.CharField(max_length=20, default='VEGETARIAN', choices=CommomChoices.foodChoices)
    photo = models.ImageField(upload_to=path_and_rename, null=True, default=None)
    upto_56kg = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    upto_62kg = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    upto_69kg = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    upto_77kg = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)
    above_77kg = models.CharField(max_length=10, default='NO', choices=CommomChoices.binaryChoices)

class Sport_All_Common_Games_Men(models.Model):
    def path_and_rename(instance, filename):
        upload_to = 'MainMeet/{}/Men/{}'.format(instance.iit_name, instance.sport_name)
        ext = filename.split('.')[-1]
        namearray = instance.student_name.split(' ')
        namelen = len(namearray)
        name = ''
        for i in range(0, namelen):
            name = name + namearray[i].capitalize()
        filename = '{}_Participant_{}_{}.{}'.format(name, instance.sport_name, instance.iit_name, ext)
        return os.path.join(upload_to, filename)

    sport_name = models.CharField(max_length=30, null=True, blank=True)
    iit_name = models.CharField(max_length=25, choices=CommomChoices.iitChoices)
    student_name = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=5, choices=CommomChoices.bloodGroupChoices)
    mobile_no = PhoneNumberField()
    email = models.EmailField()
    food = models.CharField(max_length=20, default='VEGETARIAN', choices=CommomChoices.foodChoices)
    photo = models.ImageField(upload_to=path_and_rename, null=True, default=None)

class Sport_All_Common_Games_Women(models.Model):
    def path_and_rename(instance, filename):
        upload_to = 'MainMeet/{}/Women/{}'.format(instance.iit_name, instance.sport_name)
        ext = filename.split('.')[-1]
        namearray = instance.student_name.split(' ')
        namelen = len(namearray)
        name = ''
        for i in range(0, namelen):
            name = name + namearray[i].capitalize()
        filename = '{}_Participant_{}_{}.{}'.format(name, instance.sport_name, instance.iit_name, ext)
        return os.path.join(upload_to, filename)

    sport_name = models.CharField(max_length=30, null=True, blank=True)
    iit_name = models.CharField(max_length=25, choices=CommomChoices.iitChoices)
    student_name = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=5, choices=CommomChoices.bloodGroupChoices)
    mobile_no = PhoneNumberField()
    email = models.EmailField()
    food = models.CharField(max_length=20, default='VEGETARIAN', choices=CommomChoices.foodChoices)
    photo = models.ImageField(upload_to=path_and_rename, null=True, default=None)

class debug(models.Model):
    debug_id = models.IntegerField()
    model = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = PhoneNumberField()
    mail_status = models.CharField(max_length=5, default='YES')

class Push_Notifications(models.Model):
    push_page_choice = (
        ('HomePage', 'HomePage'),
        ('LivePage', 'LivePage'),
        ('GalleryPage', 'GalleryPage'),
        ('SportsPage', 'SportsPage'),
        ('GeneralChampionship', 'GeneralChampionship'),
        ('SportAthletics', 'SportAthletics'),
        ('SportBadminton', 'SportBadminton'),
        ('SportBasketball', 'SportBasketball'),
        ('SportCricket', 'SportCricket'),
        ('SportFootball', 'SportFootball'),
        ('SportHockey', 'SportHockey'),
        ('SportSquash', 'SportSquash'),
        ('SportSwimming', 'SportSwimming'),
        ('SportTableTennis', 'SportTableTennis'),
        ('SportTennis', 'SportTennis'),
        ('SportVolleyball', 'SportVolleyball'),
        ('SportWaterpolo', 'SportWaterpolo'),
        ('SportWeightlifting', 'SportWeightlifting'),
        ('MapsHomePage', 'MapsHomePage'),
        ('MapsFreeRoam', 'MapsFreeRoam'),
        ('MapsRoot', 'MapsRoot'),
        ('ContactUsPage', 'ContactUsPage'),
        ('NotificationPage', 'NotificationPage'),
        ('OLAPedalPage', 'OLAPedalPage'),
        ('play', 'PlayStoreLink'),
        ('TodayEvent', 'TodayEvent'),
        ('FanmodePage', 'FanmodePage'),
    )
    sound_choice = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    username = models.CharField(max_length=30, blank=True, null=True)
    title = models.CharField(max_length=25, default='InterIIT')
    message = models.CharField(max_length=160)
    sound = models.CharField(max_length=5, default=None, choices=sound_choice)
    to = models.CharField(max_length=255, default='All')
    push_page = models.CharField(max_length=30, default='NotificationPage', choices=push_page_choice)
