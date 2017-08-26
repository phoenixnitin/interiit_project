from django.shortcuts import render, HttpResponse
from django.views import View
from .forms import Sports_Aquatics_Men_form, Sports_Aquatics_Women_form, Sports_Aquatics_Staff_form
from django.http import HttpResponseRedirect
from django.views.decorators.clickjacking import xframe_options_exempt
import json
# Create your views here.

class Sports_Aquatics_Men_view(View):
    @xframe_options_exempt
    def get(self, request, *args, **kwargs):
        form = Sports_Aquatics_Men_form()
        return render(request, 'register.html', {'form': form, 'heading': 'Aquatics Meet Form : Men'})

    @xframe_options_exempt
    def post(self, request, *args, **kwargs):
        form = Sports_Aquatics_Men_form(request.POST, request.FILES)
        print('self', self)
        print('request', request.POST)
        print('*args', args)
        # print('**kwargs', **kwargs)

        if form.is_valid():
            print('form is valid')
            form.save()
            return HttpResponse('Registration completed successfully')
        else:
            print('invalid form')
            return HttpResponse('Your registration is not valid. Please enter details correctly')

class Sports_Aquatics_Women_view(View):
    @xframe_options_exempt
    def get(self, request, *args, **kwargs):
        form = Sports_Aquatics_Women_form()
        return render(request, 'register.html', {'form': form, 'heading': 'Aquatics Meet Form : Women'})

    @xframe_options_exempt
    def post(self, request, *args, **kwargs):
        form = Sports_Aquatics_Women_form(request.POST, request.FILES)
        print('self', self)
        # prit ('request photo', request.POST.get('photo'))
        print('request',request.POST)
        print('*args', args)
        dictionary = request.POST.dict()
        count=0
        #print('**kwargs', **kwargs)
        if dictionary['freestyle_50m']=="YES":
            count=count+1
        if dictionary['freestyle_100m']=="YES":
            count=count+1
        if dictionary['breast_stroke_50m']=="YES":
            count=count+1
        if dictionary['back_stroke_50m']=="YES":
            count=count+1
        if dictionary['butterfly_50m']=="YES":
            count=count+1
        if dictionary['freestyle_relay_4x50m']=="YES":
            count=count+1
        print count
        if form.is_valid() and count<=3:
            print('form is valid')
            form.save()
            return HttpResponse('Registration completed successfully')
        else:
            print('invalid form')
            if count<=3:
                return HttpResponse('Your registration is not valid. Please enter details correctly')
            return HttpResponse('You can only register for a maximum of three events')
            
class Sports_Aquatics_Staff_view(View):
    @xframe_options_exempt
    def get(self, request, *args, **kwargs):
        form = Sports_Aquatics_Staff_form()
        return render(request, 'register.html', {'form': form, 'heading': 'Aquatics Meet Form : Staff'})

    @xframe_options_exempt
    def post(self, request, *args, **kwargs):
        form = Sports_Aquatics_Staff_form(request.POST, request.FILES)
        print('self', self)
        print('request', request.POST)

        print('*args', args)
        #print('**kwargs', ** kwargs)

        if form.is_valid():
            print('form is valid')
            form.save()
            return HttpResponse('Registration completed successfully')
        else:
            print('invalid form')
            return HttpResponse('Your registration is not valid. Please enter details correctly')
