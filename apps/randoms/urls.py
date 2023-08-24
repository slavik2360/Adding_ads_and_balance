from django.urls import path

from randoms.views import RandomView



urlpatterns = [
    path('', RandomView.as_view(), name='random')
]

