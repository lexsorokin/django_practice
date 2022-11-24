from django.contrib import admin
from app_market_place.models import Store, Goods, Cart


class GoodsInLine(admin.TabularInline):
    model = Goods


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['owner', 'title', 'creation_date']
    list_filter = ['owner', 'creation_date']
    inlines = [GoodsInLine]


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['title', 'creation_date', 'update_date', 'store']
    list_filter = ['store']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'good', 'add_datetime', 'good_quantity']
    list_filter = ['user']
