import random
from django.shortcuts import render
from django.views import View
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, JsonResponse
import json
from auths.models import MyUser, Transaction


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
        user_id = request.POST.get('userId')
        users: QuerySet[MyUser] = MyUser.objects.get(pk=user_id)
        result: QuerySet = request.POST.get('result')
        print('результат:', result)

        if int(result) < 0:
            transaction: Transaction = Transaction.objects.create(
                user = users,
                amount = int(result)
            )
            print("Транзакция на вычетание")
            transaction.save()
        else:
            transaction: Transaction = Transaction.objects.create(
                user = users,
                amount = int(result),
                is_filled = True
            )
            print("Транзакция на пополнение")
            transaction.save()
        
        return JsonResponse({'success': True})
    

