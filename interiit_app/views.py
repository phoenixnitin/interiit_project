from django.shortcuts import render, HttpResponse
from django.views import View
from .forms import Sports_Aquatics_Men_form, Sports_Aquatics_Women_form, Sports_Aquatics_Staff_form
from .serializer import Sport_Aquatics_Men_serializer, Sport_Aquatics_Women_serializer, Sport_Aquatics_Staff_serializer
from rest_framework import mixins, viewsets
from .models import Sport_Aquatics_Men, Sport_Aquatics_Women, Sport_Aquatics_Staff
from django.http import HttpResponseRedirect
from django.views.decorators.clickjacking import xframe_options_exempt
import json
import time
from .data import Data
from .response_message import response

# Create your views here.

def send_email(user, pwd, recipient, subject, body):
    import smtplib
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")

class Sports_Register_view(View):
    @xframe_options_exempt
    def get(self, request, sport_name, category, *args, **kwargs):
        form = None
        heading = None
        if sport_name == 'aquatics':
            if category == 'men':
                form = Sports_Aquatics_Men_form
                heading = 'Aquatics Meet Form : Men'
                print('case men')
            elif category == 'women':
                form = Sports_Aquatics_Women_form
                heading = 'Aquatics Meet Form : Women'
                print('case women')
            elif category == 'facultyandstaff':
                form = Sports_Aquatics_Staff_form
                heading = 'Aquatics Meet Form : Faculty and Staff'
                print('case staff')
            else:
                print('Category doesn\'t exist')
        else:
            print('Sport doesn\'t exist')
        #print(sport_name, category)
        if form is None:
            return HttpResponse('Registration form doesn\'t exist')
        else:
            return render(request, 'registration-form.html', {'form': form, 'heading': heading})

    @xframe_options_exempt
    def post(self, request, sport_name, category, *args, **kwargs):
        form = ''
        list = ''
        extra_text = ''
        if sport_name == 'aquatics':
            if category == 'men':
                form = Sports_Aquatics_Men_form(request.POST, request.FILES)
                list = ['free_50m', 'free_100m', 'free_200m', 'free_400m', 'free_1500m', 'back_50m',
                        'back_100m', 'back_200m', 'breast_50m', 'breast_100m', 'breast_200m', 'b_fly_50m', 'b_fly_100m',
                        'i_m_200m']
                extra_text = ', other than water polo and relays'
            elif category == 'women':
                form = Sports_Aquatics_Women_form(request.POST, request.FILES)
                list = ['freestyle_50m', 'freestyle_100m', 'breast_stroke_50m', 'back_stroke_50m', 'butterfly_50m']
                extra_text = ', other than relay'
            elif category == 'facultyandstaff':
                form = Sports_Aquatics_Staff_form(request.POST, request.FILES)
            else:
                print('Category doesn\'t exist')
        else:
            print('Sport doesn\'t exist')

        print('self', self)
        print('request', request.POST)
        print('*args', args)
        dictionary = request.POST.dict()
        count = 0
        # print('**kwargs', **kwargs)
        for item in list:
            if dictionary[item] == "YES":
                count = count + 1
        print(count)
        details = ""
        if form.is_valid():
            if category == 'staff' or count <= 3:
                print('form is valid')
                form.full_clean()
                form.save()
                recepient_email = dictionary['email']
                subject = "Registered Successfully for InterIIT Sports Meet 2017"
                message = response(dict=dictionary, category=category)
                print(message)
                data = Data()
                send_email(data.getid(),data.getpwd(),recepient_email,subject,message)
                #send_email(data.getid(),data.getpwd(),data.getrecvid(),subject,message)
                return render(request, 'registration-response.html', {
                    'message': 'Registration completed successfully. You are ready to rock at IIT Madras.',
                    'status': 'success',
                })
            else:
                print('Valid form. More than 3 entries chosen')
                return render(request, 'registration-response.html', {
                    'message': 'You can only register for a maximum of three events'+extra_text+'.',
                    'status': 'failed',
                })
        else:
            print('invalid form')
            if count <= 3:
                return render(request, 'registration-response.html', {
                    'message': 'Your registration is not valid. Please enter details correctly',
                    'status': 'failed',
                })
            return render(request, 'registration-response.html', {
                'message': 'You can only register for a maximum of three events'+extra_text+'.',
                'status': 'failed',
            })


class Register_Page(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')

class json_aquatics_men(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = Sport_Aquatics_Men_serializer
    queryset = Sport_Aquatics_Men.objects.all()

class json_aquatics_women(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = Sport_Aquatics_Women_serializer
    queryset = Sport_Aquatics_Women.objects.all()

class json_aquatics_staff(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = Sport_Aquatics_Staff_serializer
    queryset = Sport_Aquatics_Staff.objects.all()

def sendmailtoalreadyregistered_men(id=None):
    listmen = ('iit_name', 'student_name', 'blood_group', 'mobile_no', 'email', 'mode_of_transportation',
               'transport_name', 'arrival_date', 'arrival_time', 'departure_date', 'departure_time', 'food',
               'water_polo', 'free_50m', 'free_100m', 'free_200m', 'free_400m', 'free_1500m', 'back_50m', 'back_100m',
               'back_200m', 'breast_50m', 'breast_100m', 'breast_200m', 'b_fly_50m', 'b_fly_100m', 'i_m_200m',
               'free_relay_4x100m', 'medley_relay_4x100m',)
    n=len(listmen)
    if id is not None:
        queryset = Sport_Aquatics_Men.objects.values().filter(id=id)
    else:
        queryset = Sport_Aquatics_Men.objects.values()

    for object in queryset:
        #print(object, "\n\n\n")
        details = ""
        for i in range(0,n):
            if listmen[i] == 'student_name':
                details += "name : " + str(object[listmen[i]]) + "\n"
            elif listmen[i] == 'iit_name':
                details += str(object[listmen[i]]) + "\n"
            else:
                details += listmen[i]+" : "+str(object[listmen[i]])+"\n"
        #print(details, "\n")
        recepient_name = object['student_name']
        message = '''Dear {}, 
    You have successfully registered for InterIIT Sports Meet 2017.

Details:
{}

In case of any error reply to this mail. Your image is stored in our database.
'''.format(recepient_name, details)
        recepient_email = object['email']
        subject = "Registered Successfully for InterIIT Sports Meet 2017"
        data = Data()
        print(message)
        #send_email(data.getid(), data.getpwd(), recepient_email, subject, message)

def sendmailtoalreadyregistered_women(id=None):
    listwomen = ('iit_name', 'student_name', 'blood_group', 'mobile_no', 'email', 'mode_of_transportation',
                 'transport_name', 'arrival_date', 'arrival_time', 'departure_date', 'departure_time', 'food',
                 'freestyle_50m', 'freestyle_100m', 'breast_stroke_50m', 'back_stroke_50m', 'butterfly_50m',
                 'freestyle_relay_4x50m',)
    n=len(listwomen)
    if id is not None:
        queryset = Sport_Aquatics_Women.objects.values().filter(id=id)
    else:
        queryset = Sport_Aquatics_Women.objects.values()

    for object in queryset:
        details = ""
        for i in range(0,n):
            if listwomen[i] == 'student_name':
                details += "name : " + str(object[listwomen[i]]) + "\n"
            elif listwomen[i] == 'iit_name':
                details += str(object[listwomen[i]]) + "\n"
            else:
                details += listwomen[i]+" : "+str(object[listwomen[i]])+"\n"
        recepient_name = object['student_name']
        message = '''Dear {}, 
    You have successfully registered for InterIIT Sports Meet 2017.

Details:
{}

In case of any error reply to this mail. Your image is stored in our database.
'''.format(recepient_name, details)
        recepient_email = object['email']
        subject = "Registered Successfully for InterIIT Sports Meet 2017"
        data = Data()
        print(message)
        send_email(data.getid(), data.getpwd(), recepient_email, subject, message)

def sendmailtoalreadyregistered_facultyandstaff(id=None):
    listfacultyandstaff = ('iit_name', 'staff_name', 'blood_group', 'mobile_no', 'email', 'mode_of_transportation',
              'transport_name', 'arrival_date', 'arrival_time', 'departure_date', 'departure_time', 'food',
              'designation',)
    n=len(listfacultyandstaff)
    if id is not None:
        queryset = Sport_Aquatics_Staff.objects.values().filter(id=id)
    else:
        queryset = Sport_Aquatics_Staff.objects.values()

    for object in queryset:
        details = ""
        for i in range(0,n):
            if listfacultyandstaff[i] == 'staff_name':
                details += "name : " + str(object[listfacultyandstaff[i]]) + "\n"
            elif listfacultyandstaff[i] == 'iit_name':
                details += str(object[listfacultyandstaff[i]]) + "\n"
            else:
                details += listfacultyandstaff[i]+" : "+str(object[listfacultyandstaff[i]])+"\n"
        recepient_name = object['staff_name']
        message = '''Dear {}, 
    You have successfully registered for InterIIT Sports Meet 2017.

Details:
{}

In case of any error reply to this mail. Your image is stored in our database.
'''.format(recepient_name, details)
        recepient_email = object['email']
        subject = "Registered Successfully for InterIIT Sports Meet 2017"
        data = Data()
        print(message)
        send_email(data.getid(), data.getpwd(), recepient_email, subject, message)