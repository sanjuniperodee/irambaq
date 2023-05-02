from django.contrib.staticfiles.views import serve
from django.urls import path, re_path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('detail<str:slug>', detail, name='detail')
]