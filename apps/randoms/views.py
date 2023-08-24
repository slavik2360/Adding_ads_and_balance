from django.shortcuts import render
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
import random


class RandomView(View):


    def get(self, request: HttpRequest) -> HttpResponse:
        a = random.randint(-100, 100)
        return render(
            request=request,
            template_name='random/wheel.html',
            context={
                'a': a
            }
        )


