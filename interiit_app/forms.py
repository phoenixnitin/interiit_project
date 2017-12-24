from django.forms import ModelForm
from .models import Sport_Aquatics_Men, Sport_Aquatics_Women, Sport_Aquatics_Staff, Staff, Sport_Athletics_Men, Sport_Athletics_Women, Sport_Weightlifting, Sport_All_Common_Games_Men, Sport_All_Common_Games_Women, Push_Notifications
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget

class Sports_Aquatics_Men_form(ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = Sport_Aquatics_Men
        fields = '__all__'
        labels = {
            "iit_name": _('IIT'),
            "student_name": _('Name'),
            "blood_group": _('Blood Group'),
            "mobile_no": _('Contact No.'),
            "email": _('E-mail'),
            "photo": _('Photo'),
            "mode_of_transportation": _('Mode of Transportation'),
            "transport_name": _('Flight/Train Name'),
            "arrival_date": _('Arrival Date'),
            "arrival_time": _('Arrival Time'),
            "departure_date": _('Departure Date'),
            "departure_time": _('Departure Time'),
            "food": _('Food'),
            "free_50m": _('50m Free'),
            "free_100m": _('100m Free'),
            "free_200m": _('200m Free'),
            "free_400m": _('400m Free'),
            "free_1500m": _('1500m Free'),
            "back_50m": _('50m Back'),
            "back_100m": _('100m Back'),
            "back_200m": _('200m Back'),
            "breast_50m": _('50m Breast'),
            "breast_100m": _('100m Breast'),
            "breast_200m": _('200m Breast'),
            "b_fly_50m": _('50m Butterfly'),
            "b_fly_100m": _('100m Butterfly'),
            "i_m_200m": _('200m I.M.'),
            "free_relay_4x100m": _('4x100m Freestyle Relay'),
            "medley_relay_4x100m": _('4x100m Medley Relay'),
        }
        widgets = {
            'mobile_no': PhoneNumberInternationalFallbackWidget,
        }
        help_texts = {
            'mobile_no': _('Please enter your country code, if not from India'),
            'photo': _('Please upload passport size photo'),
            'arrival_date': _('Please enter in format: DD-MM-YYYY'),
            'departure_date': _('Please enter in format: DD-MM-YYYY'),
            'arrival_time': _('Please enter in format HH:MM AM/PM'),
            'departure_time': _('Please enter in format HH:MM AM/PM'),
        }

class Sports_Aquatics_Women_form(ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = Sport_Aquatics_Women
        fields = '__all__'
        labels = {
            "iit_name": _('IIT'),
            "student_name": _('Name'),
            "blood_group": _('Blood Group'),
            "mobile_no": _('Contact No.'),
            "email": _('E-mail'),
            "photo": _('Photo'),
            "mode_of_transportation": _('Mode of Transportation'),
            "transport_name": _('Flight/Train Name'),
            "arrival_date": _('Arrival Date'),
            "arrival_time": _('Arrival Time'),
            "departure_date": _('Departure Date'),
            "departure_time": _('Departure Time'),
            "food": _('Food'),
            "freestyle_50m": _('50m Freestyle'),
            "freestyle_100m": _('100m Freestyle'),
            "breast_stroke_50m": _('50m Breast Stroke'),
            "back_stroke_50m": _('50m Back Stroke'),
            "butterfly_50m": _('50m Butterfly'),
            "freestyle_relay_4x50m": _('4x50m Freestyle Relay'),
        }
        widgets = {
            'mobile_no': PhoneNumberInternationalFallbackWidget,
        }
        help_texts = {
            'mobile_no': _('Please enter your country code, if not from India'),
            'photo': _('Please upload passport size photo'),
            'arrival_date': _('Please enter in format: DD-MM-YYYY'),
            'departure_date': _('Please enter in format: DD-MM-YYYY'),
            'arrival_time': _('Please enter in format HH:MM AM/PM'),
            'departure_time': _('Please enter in format HH:MM AM/PM'),
        }

class Sports_Aquatics_Staff_form(ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = Sport_Aquatics_Staff
        fields = '__all__'
        labels = {
            "iit_name": _('IIT'),
            "staff_name": _('Name'),
            "gender": _('Gender'),
            "blood_group": _('Blood Group'),
            "mobile_no": _('Contact No.'),
            "email": _('E-mail'),
            "photo": _('Photo'),
            "mode_of_transportation": _('Mode of Transportation'),
            "transport_name": _('Flight/Train Name'),
            "arrival_date": _('Arrival Date'),
            "arrival_time": _('Arrival Time'),
            "departure_date": _('Departure Date'),
            "departure_time": _('Departure Time'),
            "food": _('Food'),
            "designation": _('Designation'),
        }
        widgets = {
            'mobile_no': PhoneNumberInternationalFallbackWidget,
        }
        help_texts = {
            'mobile_no': _('Please enter your country code, if not from India'),
            'photo': _('Please upload passport size photo'),
            'arrival_date': _('Please enter in format: DD-MM-YYYY'),
            'departure_date': _('Please enter in format: DD-MM-YYYY'),
            'arrival_time': _('Please enter in format HH:MM AM/PM'),
            'departure_time': _('Please enter in format HH:MM AM/PM'),
        }
        
class Staff_form(ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = Staff
        fields = '__all__'
        hidden_fields = ('sport_name',)
        labels = {
            "sport_name": _('Sport Name'),
            "iit_name": _('IIT'),
            "staff_name": _('Name'),
            "gender": _('Gender'),
            "blood_group": _('Blood Group'),
            "mobile_no": _('Contact No.'),
            "email": _('E-mail'),
            "photo": _('Photo'),
            "food": _('Food'),
            "designation": _('Designation'),
        }
        widgets = {
            'mobile_no': PhoneNumberInternationalFallbackWidget,
        }
        help_texts = {
            'mobile_no': _('Please enter your country code, if not from India'),
            'photo': _('Please upload passport size photo'),
        }

class Sports_Athletics_Men_form(ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    class Meta:
        model = Sport_Athletics_Men
        fields = '__all__'
        labels = {
            "iit_name": _('IIT'),
            "student_name": _('Name'),
            "blood_group": _('Blood Group'),
            "mobile_no": _('Contact No.'),
            "email": _('E-mail'),
            "photo": _('Photo'),
            "food": _('Food'),
            "_100m": _('100m'),
            "_200m": _('200m'),
            "_400m": _('400m'),
            "_800m": _('800m'),
            "_1500m": _('1500m'),
            "_5000m": _('5000m'),
            "hurdles_110m": _('110m Hurdles'),
            "hurdles_400m": _('400m Hurdles'),
            "high_jump": _('High Jump'),
            "long_jump": _('Long Jump'),
            "triple_jump": _('Triple Jump'),
            "pole_vault": _('Pole Vault'),
            "shot_put": _('Shot Put'),
            "discuss_throw": _('Discuss Throw'),
            "javelin_throw": _('Javelin Throw'),
            "hammer_throw": _('Hammer Throw'),
            "relay_4x100m": _('4x100m Relay'),
            "relay_4x400m": _('4x400m Relay'),
        }
        widgets = {
            'mobile_no': PhoneNumberInternationalFallbackWidget,
        }
        help_texts = {
            'mobile_no': _('Please enter your country code, if not from India'),
            'photo': _('Please upload passport size photo'),
        }

class Sports_Athletics_Women_form(ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = Sport_Athletics_Women
        fields = '__all__'
        labels = {
            "iit_name": _('IIT'),
            "student_name": _('Name'),
            "blood_group": _('Blood Group'),
            "mobile_no": _('Contact No.'),
            "email": _('E-mail'),
            "photo": _('Photo'),
            "food": _('Food'),
            "_100m": _('100m'),
            "_200m": _('200m'),
            "_400m": _('400m'),
            "_800m": _('800m'),
            "_1500m": _('1500m'),
            "high_jump": _('High Jump'),
            "long_jump": _('Long Jump'),
            "shot_put": _('Shot Put'),
            "discuss_throw": _('Discuss Throw'),
            "relay_4x100m": _('4x100m Relay'),
            "relay_4x400m": _('4x400m Relay'),
        }
        widgets = {
            'mobile_no': PhoneNumberInternationalFallbackWidget,
        }
        help_texts = {
            'mobile_no': _('Please enter your country code, if not from India'),
            'photo': _('Please upload passport size photo'),
        }

class Sports_Weightlifting_form(ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    class Meta:
        model = Sport_Weightlifting
        fields = '__all__'
        labels = {
            "iit_name": _('IIT'),
            "student_name": _('Name'),
            "blood_group": _('Blood Group'),
            "mobile_no": _('Contact No.'),
            "email": _('E-mail'),
            "photo": _('Photo'),
            "food": _('Food'),
            "upto_56kg": _('Upto 56kg'),
            "upto_62kg": _('Upto 62kg'),
            "upto_69kg": _('Upto 69kg'),
            "upto_77kg": _('Upto 77kg'),
            "above_77kg": _('Above 77kg'),
        }
        widgets = {
            'mobile_no': PhoneNumberInternationalFallbackWidget,
        }
        help_texts = {
            'mobile_no': _('Please enter your country code, if not from India'),
            'photo': _('Please upload passport size photo'),
        }

class Sport_All_Common_Games_Men_form(ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    class Meta:
        model = Sport_All_Common_Games_Men
        fields = '__all__'
        labels = {
            "iit_name": _('IIT'),
            "student_name": _('Name'),
            "blood_group": _('Blood Group'),
            "mobile_no": _('Contact No.'),
            "email": _('E-mail'),
            "photo": _('Photo'),
            "food": _('Food'),
        }
        widgets = {
            'mobile_no': PhoneNumberInternationalFallbackWidget,
        }
        help_texts = {
            'mobile_no': _('Please enter your country code, if not from India'),
            'photo': _('Please upload passport size photo'),
        }

class Sport_All_Common_Games_Women_form(ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    class Meta:
        model = Sport_All_Common_Games_Women
        fields = '__all__'
        labels = {
            "iit_name": _('IIT'),
            "student_name": _('Name'),
            "blood_group": _('Blood Group'),
            "mobile_no": _('Contact No.'),
            "email": _('E-mail'),
            "photo": _('Photo'),
            "food": _('Food'),
        }
        widgets = {
            'mobile_no': PhoneNumberInternationalFallbackWidget,
        }
        help_texts = {
            'mobile_no': _('Please enter your country code, if not from India'),
            'photo': _('Please upload passport size photo'),
        }

from django import forms
class Push_Notification_form(ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    class Meta:
        model = Push_Notifications
        fields = '__all__'
        help_texts = {
            'title': _('Enter title of notification'),
            'message': _('Enter body of notification'),
            'sound': _('receiving device should give sound or not'),
            'to': _('Who is the receiver'),
            'push_page': _('This page will be pushed in the device when notification is clicked.'),
        }
        widgets = {
            'message': forms.Textarea(attrs={'rows': "6"})
        }