from django.urls import path, include
from django.contrib import admin
from main.views import main_page
from randoms.views import RandomView


urlpatterns=[
    path('',main_page, name='main'),
    path('random/', RandomView.as_view(), name='random')   
]