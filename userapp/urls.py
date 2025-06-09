from django.urls import path
from .views import *

urlpatterns = [
    
    path('',hh,name="hh"),
    path('register/',register,name="register"),
    path("home",home,name="home"),
    path("login/",loginview,name="login"),
    path("logout/",logoutview,name="logout"),
    path("lg/",lang,name="lg"),
    path("helpspt",helSupport,name="helpspt"),
    path("settings",Settings,name="settings"),
    path("live-chat",Livechat,name="live-chat"),
    path('friend-request/send/<int:user_id>/', send_friend_request, name='send_friend_request'),
    path('friend-request/accept/<int:request_id>/', accept_friend_request, name='accept_friend_request'),
    path('podcasts',podcs,name="podcasts")

]
