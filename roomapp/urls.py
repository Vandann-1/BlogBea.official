from django.urls import path
from roomapp.views import *

urlpatterns = [
    path('blog_discussion/<slug:blog_slug>/', join_discussion, name='blog_discussion'),

    # path('blog/<slug:slug>/',blog_detail, name='blog_detail'),



]
