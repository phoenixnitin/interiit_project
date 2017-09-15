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
        if form.is_valid():
            if category == 'staff' or count <= 3:
                if(category == "staff"):
                    recepient_name = dictionary["staff_name"]
                else:
                    recepient_name = dictionary["student_name"]       
                print('form is valid')
                form.save()
                recepient_email = dictionary["email"]
                message = '''
Dear {}, 
    You have successfully registered for InterIIT Sports Meet 2017.'''.format(recepient_name)
                send_email("<sender email>","<secret code>",recepient_email,"[No-Reply]",message)
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
