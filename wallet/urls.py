from django.urls import path

from .views import register_card, register_customer,register_account, register_loan, register_notification, register_receipt, register_reward, register_thirdparty

urlpatterns = [
    path("register/", register_customer, name= "registration"),
    path("account/",register_account,name="account"),
     # path("wallets/",register_wallet,name="wallet"),
      # path("transaction/",register_transaction,name="transaction"),
    path("card/",register_card,name="card"),
    path("thirdparty/",register_thirdparty,name="thirdparty"),
    path("receipt/",register_receipt,name="receipt"),
    path("notification/",register_notification,name="notification"),
    path("loan/",register_loan,name="loan"),
    path("reward/",register_reward,name="reward"),
   

    ]
