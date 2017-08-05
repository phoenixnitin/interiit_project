from django.conf.urls import url
from .views import Sports_Aquatics_Men_view, Sports_Aquatics_Women_view, Sports_Aquatics_Staff_view

urlpatterns = [
    url(r'^sport/aquatics/men/$', Sports_Aquatics_Men_view.as_view(), name='aquatics_men'),
    url(r'^sport/aquatics/women/$', Sports_Aquatics_Women_view.as_view(), name='aquatics_women'),
    url(r'^sport/aquatics/staff/$', Sports_Aquatics_Staff_view.as_view(), name='aquatics_staff'),
]