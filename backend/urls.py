from django.urls import path
from django.urls import include
from backend import views

urlpatterns = [
    path('api/v1/init', views.InitialiseWallet.as_view(), name='intialisewallet'),
    path('api/v1/wallet', views.WalletView.as_view(), name='wallet'),
    path('api/v1/wallet/deposits', views.DepositToWallet.as_view(), name='TopUpmoneytowallet'),
    path('api/v1/wallet/withdrawals',views.WithdrawalFromWallet.as_view(), name='usemoneyfromwallet'),
]