from django.shortcuts import render
from django.conf import settings

from auths.models import Ad
from django.utils import timezone

def main_page(request):
    ads = Ad.objects.all()
    print(ads)
    return render(
        template_name='main.html',
        request=request,
        context={
            'ads': ads
        }
        )