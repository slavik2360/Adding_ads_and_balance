from django.contrib import admin
from .models import (
    MyUser,
    ActivationCode,
    BankCard,
    Transaction,
    Ad
)


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display:list[str] = (
        'email',
        'nickname',
        'currency',
    )
    list_filter: list[str] = (
        'nickname',
    ) 


@admin.register(ActivationCode)
class CodeAdmin(admin.ModelAdmin):
    list_display:list[str] = (
        'code',
        'datetime_created'
    )
    list_filter: list[str] = (
        'user',
    )



@admin.register(BankCard)
class BancCardAdmin(admin.ModelAdmin):
    list_display:list[str] = (
        'number',
        'owner',
        'experation_time',
        'cvv'
    )
    list_filter: list[str] = (
        'owner',
    )


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display:list[str] = (
        'amount',
        'datetime_created',
        'is_filled',
    )
    list_filter: list[str] = (
        'user',
    )


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date', 'is_active']