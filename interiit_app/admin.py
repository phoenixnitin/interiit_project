from django.contrib import admin
from .models import Sport_Aquatics_Men, Sport_Aquatics_Women, Sport_Aquatics_Staff, Sport_Weightlifting, Staff, Sport_Athletics_Men, Sport_Athletics_Women, Sport_All_Common_Games_Men, Sport_All_Common_Games_Women

# Register your models here.
class AdminModel_Sport_Aquatics_Men(admin.ModelAdmin):
    mylist = ('id', 'iit_name', 'student_name', 'blood_group', 'mobile_no', 'email', 'photo', 'mode_of_transportation',
              'transport_name', 'arrival_date', 'arrival_time', 'departure_date', 'departure_time', 'food',
              'water_polo', 'free_50m', 'free_100m', 'free_200m', 'free_400m', 'free_1500m', 'back_50m', 'back_100m',
              'back_200m', 'breast_50m', 'breast_100m', 'breast_200m', 'b_fly_50m', 'b_fly_100m', 'i_m_200m',
              'free_relay_4x100m', 'medley_relay_4x100m',)
    list_display = mylist
    list_display_links = mylist
    list_filter = mylist
    search_fields = mylist

class AdminModel_Sport_Aquatics_Women(admin.ModelAdmin):
    mylist = ('id', 'iit_name', 'student_name', 'blood_group', 'mobile_no', 'email', 'photo', 'mode_of_transportation',
              'transport_name', 'arrival_date', 'arrival_time', 'departure_date', 'departure_time', 'food',
              'freestyle_50m', 'freestyle_100m', 'breast_stroke_50m', 'back_stroke_50m', 'butterfly_50m',
              'freestyle_relay_4x50m',)
    list_display = mylist
    list_display_links = mylist
    list_filter = mylist
    search_fields = mylist

class AdminModel_Sport_Aquatics_FacultyandStaff(admin.ModelAdmin):
    mylist = ('id', 'iit_name', 'staff_name', 'blood_group', 'mobile_no', 'email', 'photo', 'mode_of_transportation',
              'transport_name', 'arrival_date', 'arrival_time', 'departure_date', 'departure_time', 'food',
              'designation',)
    list_display = mylist
    list_display_links = mylist
    list_filter = mylist
    search_fields = mylist

# admin.site.register(Sport_Aquatics_Men, AdminModel_Sport_Aquatics_Men)
# admin.site.register(Sport_Aquatics_Women, AdminModel_Sport_Aquatics_Women)
# admin.site.register(Sport_Aquatics_Staff, AdminModel_Sport_Aquatics_FacultyandStaff)

class AdminModel_Sport_Weightlifting(admin.ModelAdmin):
    mylist = ('id', 'iit_name', 'student_name', 'blood_group', 'mobile_no', 'email', 'photo', 'food','upto_56kg','upto_62kg','upto_69kg',
              'upto_77kg','above_77kg',)
    list_display = mylist
    list_display_links = mylist
    list_filter = mylist
    search_fields = mylist
admin.site.register(Sport_Weightlifting, AdminModel_Sport_Weightlifting)

class AdminModel_Sport_All_Staff(admin.ModelAdmin):
    mylist = ('id', 'iit_name', 'staff_name', 'sport_name', 'blood_group', 'mobile_no', 'email', 'photo', 'food', 'designation',)
    list_display = mylist
    list_display_links = mylist
    list_filter = mylist
    search_fields = mylist
admin.site.register(Staff, AdminModel_Sport_All_Staff)

class AdminModel_Sport_Athletics_Men(admin.ModelAdmin):
    mylist = ('id', 'iit_name', 'student_name', 'blood_group', 'mobile_no', 'email', 'photo', 'food',
              '_100m', '_200m', '_400m', '_800m', '_1500m', '_5000m', 'hurdles_110m', 'hurdles_400m','high_jump',
              'long_jump', 'triple_jump', 'pole_vault', 'shot_put', 'discuss_throw', 'javelin_throw', 'hammer_throw',
              'relay_4x100m', 'relay_4x400m')
    list_display = mylist
    list_display_links = mylist
    list_filter = mylist
    search_fields = mylist
admin.site.register(Sport_Athletics_Men, AdminModel_Sport_Athletics_Men)

class AdminModel_Sport_Athletics_Women(admin.ModelAdmin):
    mylist = ('id', 'iit_name', 'student_name', 'blood_group', 'mobile_no', 'email', 'photo', 'food',
              '_100m', '_200m', '_400m', '_800m', '_1500m', 'high_jump', 'long_jump', 'shot_put', 'discuss_throw',
              'relay_4x100m', 'relay_4x400m')
    list_display = mylist
    list_display_links = mylist
    list_filter = mylist
    search_fields = mylist
admin.site.register(Sport_Athletics_Women, AdminModel_Sport_Athletics_Women)

class AdminModel_Sport_All_Common_Sports(admin.ModelAdmin):
    mylist = ('id', 'iit_name', 'student_name', 'sport_name', 'blood_group', 'mobile_no', 'email', 'photo', 'food',)
    list_display = mylist
    list_display_links = mylist
    list_filter = mylist
    search_fields = mylist
admin.site.register(Sport_All_Common_Games_Men, AdminModel_Sport_All_Common_Sports)
admin.site.register(Sport_All_Common_Games_Women, AdminModel_Sport_All_Common_Sports)