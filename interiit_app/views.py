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
            elif category == 'staff':
                form = Sports_Aquatics_Staff_form
                heading = 'Aquatics Meet Form : Staff'
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
        if sport_name == 'aquatics':
            if category == 'men':
                form = Sports_Aquatics_Men_form(request.POST, request.FILES)
                list = ['free_50m', 'free_100m', 'free_200m', 'free_400m', 'free_1500m', 'back_50m',
                        'back_100m', 'back_200m', 'breast_50m', 'breast_100m', 'breast_200m', 'b_fly_50m', 'b_fly_100m',
                        'i_m_200m']
            elif category == 'women':
                form = Sports_Aquatics_Women_form(request.POST, request.FILES)
                list = ['freestyle_50m', 'freestyle_100m', 'breast_stroke_50m', 'back_stroke_50m', 'butterfly_50m']
            elif category == 'staff':
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
                print('form is valid')
                form.save()
                return HttpResponse('Registration completed successfully')
            else:
                print('Valid form. More than 3 entries chosen')
                return HttpResponse('You can only register for a maximum of three events')
        else:
            print('invalid form')
            if count <= 3:
                return HttpResponse('Your registration is not valid. Please enter details correctly')
            return HttpResponse('You can only register for a maximum of three events')

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
