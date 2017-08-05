from django.forms import ModelForm
from .models import Sport_Aquatics_Men, Sport_Aquatics_Women, Sport_Aquatics_Staff
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab

class Sports_Aquatics_Men_form(ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = Sport_Aquatics_Men
        fields = '__all__'
        labels = {
            "iit_name": _('IIT'),
            "staff_name": _('Name'),
            "blood_group": _('Blood Group'),
            "mobile_no": _('Contact No.'),
            "email": _('E-mail'),
            "photo": _('Photo'),
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
        },
        widgets = {
            'mobile_no': PhoneNumberPrefixWidget,
        }

class Sports_Aquatics_Women_form(ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = Sport_Aquatics_Women
        fields = '__all__'
        labels = {
            "iit_name": _('IIT'),
            "staff_name": _('Name'),
            "blood_group": _('Blood Group'),
            "mobile_no": _('Contact No.'),
            "email": _('E-mail'),
            "photo": _('Photo'),
            "food": _('Food'),
            "freestyle_50m": _('50m Freestyle'),
            "freestyle_100m": _('100m Freestyle'),
            "breast_stroke_50m": _('50m Breast Stroke'),
            "back_stroke_50m": _('50m Back Stroke'),
            "butterfly_50m": _('50m Butterfly'),
            "freestyle_relay_4x50m": _('4x50m Freestyle Relay'),
        },
        widgets = {
            'mobile_no': PhoneNumberPrefixWidget,
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
            "food": _('Food'),
            "designation": _('Designation'),
        },
        widgets = {
            'mobile_no': PhoneNumberPrefixWidget,
        }