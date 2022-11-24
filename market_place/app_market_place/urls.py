from django.urls import path
from app_market_place.views import StoreList, StoreGoodsDetail, AddGoodQuantityToCart, DepositFunds, \
    CartDisplay, PaymentForOrder, Report

urlpatterns = [
    path('stores/', StoreList.as_view()),
    path('store/<int:pk>', StoreGoodsDetail.as_view()),
    path('good/add_to_cart/<int:pk>', AddGoodQuantityToCart.as_view()),
    path('profile/deposit/', DepositFunds.as_view()),
    path('my_cart/', CartDisplay.as_view()),
    path('profile/<int:pk>/cart_payment/', PaymentForOrder.as_view()),
    path('report/', Report.as_view())
]
