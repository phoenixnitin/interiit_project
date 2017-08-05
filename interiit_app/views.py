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
        return render(request, 'register.html', {'form':form, 'heading': 'Aquatics Meet Form'})

    @xframe_options_exempt
    def post(self, request, *args, **kwargs):
        #request_params = json.loads(str(request.body.decode('utf-8')))
        # data = request.POST.copy()
        # data['photo'] = '1234.jpg'
        # data.photo
        form = Sports_Aquatics_Men_form(request.POST, request.FILES)
        print ('self', self)
        print ('request', request.POST)
        # print ('request photo', request.POST.get('photo'))
        print ('*args', args)
        print ('**kwargs', ** kwargs)
        # form.save()
        # if form.is_valid():

        # return HttpResponse('post method is called')
        if form.is_valid():
            print ('form is valid')
            form.save()
            return HttpResponse('post method is called')
        else:
            print ('invalid form')
            return HttpResponseRedirect('/sport/aquatics/men/')

class Sports_Aquatics_Women_view(View):
    @xframe_options_exempt
    def get(self, request, *args, **kwargs):
        form = Sports_Aquatics_Women_form()
        return render(request, 'register.html', {'form':form, 'heading': 'Aquatics Meet Form'})

    @xframe_options_exempt
    def post(self, request, *args, **kwargs):
        #request_params = json.loads(str(request.body.decode('utf-8')))
        # data = request.POST.copy()
        # data['photo'] = '1234.jpg'
        # data.photo
        form = Sports_Aquatics_Women_form(request.POST, request.FILES)
        print ('self', self)
        print ('request', request.POST)
        # print ('request photo', request.POST.get('photo'))
        print ('*args', args)
        print ('**kwargs', ** kwargs)
        # form.save()
        # if form.is_valid():

        # return HttpResponse('post method is called')
        if form.is_valid():
            print ('form is valid')
            form.save()
            return HttpResponse('post method is called')
        else:
            print ('invalid form')
            return HttpResponseRedirect('/sport/aquatics/women/')

class Sports_Aquatics_Staff_view(View):
    @xframe_options_exempt
    def get(self, request, *args, **kwargs):
        form = Sports_Aquatics_Staff_form()
        return render(request, 'register.html', {'form':form, 'heading': 'Aquatics Meet Form'})

    @xframe_options_exempt
    def post(self, request, *args, **kwargs):
        #request_params = json.loads(str(request.body.decode('utf-8')))
        # data = request.POST.copy()
        # data['photo'] = '1234.jpg'
        # data.photo
        form = Sports_Aquatics_Staff_form(request.POST, request.FILES)
        print ('self', self)
        print ('request', request.POST)
        # print ('request photo', request.POST.get('photo'))
        print ('*args', args)
        print ('**kwargs', ** kwargs)
        # form.save()
        # if form.is_valid():

        # return HttpResponse('post method is called')
        if form.is_valid():
            print ('form is valid')
            form.save()
            return HttpResponse('post method is called')
        else:
            print ('invalid form')
            return HttpResponseRedirect('/sport/aquatics/staff/')