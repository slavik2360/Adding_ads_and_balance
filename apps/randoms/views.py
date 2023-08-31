import random
from django.shortcuts import render
from django.views import View
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, JsonResponse
import json


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
    
    def post(self, request: HttpRequest) -> JsonResponse:
        result: QuerySet = request.POST.get('result')
        print('результат:', result)

        return JsonResponse({'result': True})
    

