from django.urls import path

from auths.views import AdView, AddMoney


urlpatterns = [
    path('', AdView.as_view(), name='ads'),
    path('money/', AddMoney.as_view(), name='money' )
]

