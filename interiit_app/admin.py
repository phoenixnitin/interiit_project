from django.contrib import admin
from .models import Sport_Aquatics_Men, Sport_Aquatics_Women, Sport_Aquatics_Staff

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

admin.site.register(Sport_Aquatics_Men, AdminModel_Sport_Aquatics_Men)
admin.site.register(Sport_Aquatics_Women, AdminModel_Sport_Aquatics_Women)
admin.site.register(Sport_Aquatics_Staff, AdminModel_Sport_Aquatics_FacultyandStaff)

