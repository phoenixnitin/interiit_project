from django.conf.urls import url
from . import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import spreadsheetToJSON

urlpatterns = [
    url(r'^$', views.Redirect_To_Register_Page),
    url(r'^sport/(?P<sport_name>[a-zA-Z0-9_.-]+)/(?P<category>[a-zA-Z0-9_.-]+)/$', views.Sports_Register_view.as_view(), name='sports_register'),
    url(r'^sport/register/$', views.Register_Page.as_view(), name='register-page'),
    url(r'^download/$', views.Download_JSON, name='download-json'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login?next=/download/'}, name='logoutDownload'),
    url(r'^logout-push/$', auth_views.logout, {'next_page': '/login?next=/push-notification/'}, name='logoutPush'),
    url(r'^logout-already-sent/$', auth_views.logout, {'next_page': '/login?next=/already-sent-notification/'}, name='alreadySentNotification'),
    url(r'^push-notification/$', login_required(views.push_notification_view.as_view()), name='push-notification'),
    url(r'^already-sent-notification/$', login_required(views.Already_Sent_Notification), name='already-sent-notification'),
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