from django.conf.urls import url
from . import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.Redirect_To_Register_Page),
    url(r'^sport/(?P<sport_name>[a-zA-Z0-9_.-]+)/(?P<category>[a-zA-Z0-9_.-]+)/$', views.Sports_Register_view.as_view(), name='sports_register'),
    url(r'^sport/register/$', views.Register_Page.as_view(), name='register-page'),
    url(r'^download/$', views.Download_JSON, name='download-json'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
router = routers.SimpleRouter()
router.register(r'sport/download/aquatics/men', views.json_aquatics_men, 'json_aquatics_men')
router.register(r'sport/download/aquatics/women', views.json_aquatics_women, 'json_aquatics_women')
router.register(r'sport/download/aquatics/facultyandstaff', views.json_aquatics_staff, 'json_aquatics_staff')
router.register(r'download/weightlifting', views.json_weightlifting, 'json_weightlifting')
router.register(r'download/athletics/men', views.json_athletics_men, 'json_athletics_men')
router.register(r'download/athletics/women', views.json_athletics_women, 'json_athletics_women')
router.register(r'download/staff', views.json_staff, 'json_staff')
router.register(r'download/other_games/men', views.json_sport_all_other_games_men, 'json_sport_all_other_games_men')
router.register(r'download/other_games/women', views.json_sport_all_other_games_women, 'json_sport_all_other_games_women')

urlpatterns += router.urls