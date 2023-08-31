from django.urls import path
from .views import RandomView

urlpatterns = [
    path('', RandomView.as_view(), name='random'),
]
