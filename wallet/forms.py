
from django import forms
from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty

from django.forms import ModelForm

class CustomerRegistrationsForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class AccountRegistrationsForm(ModelForm):
    class Meta:
        model = Account
        fields = "__all__"

    
# class WalletRegistrationsForm(ModelForm):
#     class Meta:
#         model = Wallet
#         fields = "__all__"



# class TransactionRegistrationsForm(ModelForm):
#     class Meta:
#         model = Transaction
#         fields = "__all__"


class CardRegistrationsForm(ModelForm):
    class Meta:
        model = Card
        fields = "__all__"

class ThirdPartyRegistrationsForm(ModelForm):
    class Meta:
        model = ThirdParty
        fields = "__all__"

        
class ReceiptRegistrationsForm(ModelForm):
    class Meta:
        model = Receipt
        fields = "__all__"


class NotificationRegistrationsForm(ModelForm):
    class Meta:
        model = Notification
        fields = "__all__"


class LoanRegistrationsForm(ModelForm):
    class Meta:
        model = Loan
        fields = "__all__"

class RewardRegistrationsForm(ModelForm):
    class Meta:
        model = Reward
        fields = "__all__"
