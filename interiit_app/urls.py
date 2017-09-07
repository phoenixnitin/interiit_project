from django.conf.urls import url
from . import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^sport/(?P<sport_name>[a-zA-Z0-9_.-]+)/(?P<category>[a-zA-Z0-9_.-]+)/$', views.Sports_Register_view.as_view(), name='sports_register'),
    url(r'^sport/register/$', views.Register_Page.as_view(), name='register-page'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
router = routers.SimpleRouter()
router.register(r'sport/download/aquatics/men', views.json_aquatics_men, 'json_aquatics_men')
router.register(r'sport/download/aquatics/women', views.json_aquatics_women, 'json_aquatics_women')
router.register(r'sport/download/aquatics/facultyandstaff', views.json_aquatics_staff, 'json_aquatics_staff')

urlpatterns += router.urls