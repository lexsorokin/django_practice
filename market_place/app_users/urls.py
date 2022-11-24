from django.urls import path
from .views import Login, Logout, registration_view, AccountInfo, PurchaseHistory

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('registration/', registration_view, name='registration'),
    path('profile/<int:pk>/account_info/', AccountInfo.as_view()),
    path('profile/<int:pk>/purchase_history', PurchaseHistory.as_view()),
]