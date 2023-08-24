from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.db.models.query import QuerySet
from django.views.generic import View
from django.utils import timezone
from decimal import Decimal

# Create your views here.

from .models import Ad, MyUser, Transaction


class AdView(View):
    
    def get(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'ad.html'
        ads: QuerySet[Ad] = Ad.objects.all()
        print(ads)
        return render(
            request=request,
            template_name=template_name,
            context={
                'ads': ads
            }
        )
    



class AddMoney(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'addMoney.html'
        bb = MyUser().get_balance
        return render(
            request=request,
            template_name=template_name,
            context={
                'Foo':'Bar',
                'balance' : bb
            }
        )
    
    def post(self, request: HttpRequest) -> HttpResponse:
        us = request.user.id
        users: QuerySet[MyUser] = MyUser.objects.get(pk=us)
        data: dict = request.POST
        
        try:
            transaction: Transaction = Transaction.objects.create(
                user = users,
                amount = float(data.get('money')),
                is_filled = data.get('bolean')
            )
            transaction.save()
        except ValueError:
            return HttpResponse("Нужны цифры тут защита от дурака")
        return HttpResponse("Topped Up or Spent")


