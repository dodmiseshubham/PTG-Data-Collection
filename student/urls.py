from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views as student_views
urlpatterns =[

	url(r'^$', student_views.home, name ='home'),
    url(r'^search/$', student_views.search, name='search'),
    url(r'^teacher/$', student_views.teacher, name='teacher'),
]
