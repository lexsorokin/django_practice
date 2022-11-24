from django.contrib import admin
from .models import Profile, PurchasedGoods


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'email', 'phone', 'address', 'balance']
    list_filter = ['user']

    def mark_as_basic(self, request, queryset):
        queryset.update(status='b')

    def mark_as_vip(self, request, queryset):
        queryset.update(status='v')

    mark_as_basic.short_description = 'Перевести в статус Базовый'
    mark_as_vip.short_description = 'Перевести в статус VIP'


@admin.register(PurchasedGoods)
class UserPurchaseHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'good', 'purchase_date', 'purchase_sum']
    list_filter = ['user']
