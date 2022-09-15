from django.shortcuts import render
from .forms import AccountRegistrationsForm, CardRegistrationsForm, CustomerRegistrationsForm, LoanRegistrationsForm, NotificationRegistrationsForm, ReceiptRegistrationsForm, RewardRegistrationsForm, ThirdPartyRegistrationsForm, TransactionRegistrationsForm, WalletRegistrationsForm
from .models import Customer
from . import forms

# Create your views here.

def register_customer(request):
    if request.method == "Post":
        form = CustomerRegistrationsForm(request.Post)
        if form.is_valid():
            form.save()

    else:
        form = CustomerRegistrationsForm()
    
    return render(request,"wallet/register_customer.html",
    {"form":form})


    # form = CustomerRegistrationsForm()
    # return render(request,"wallet/register_customer.html",
    # {"form":form})
    

def register_account(request):
    form = AccountRegistrationsForm()
    return render(request,"wallet/register_account.html",
    {"form":form})




def register_wallet(request):
    form = WalletRegistrationsForm()
    return render(request,"wallet/register_wallet.html",
    {"form": form})

def register_transaction(request):
    form = TransactionRegistrationsForm()
    return render(request,"wallet/register_transaction.html",
    {"form":form})


def register_card(request):
    form = CardRegistrationsForm()
    return render(request,"wallet/register_card.html",
    {"form":form})


def register_thirdparty(request):
    form = ThirdPartyRegistrationsForm()
    return render(request,"wallet/register_third.html",
    {"form":form})


def register_receipt(request):
    form = ReceiptRegistrationsForm()
    return render(request,"wallet/register_receipt.html",
    {"form":form})


def register_notification(request):
    form = NotificationRegistrationsForm()
    return render(request,"wallet/register_notification.html",
    {"form":form})

def register_loan(request):
    form = LoanRegistrationsForm()
    return render(request,"wallet/register_loan.html",
    {"form":form})


def register_reward(request):
    form = RewardRegistrationsForm()
    return render(request,"wallet/register_reward.html",
    {"form":form})

def list_customers(request):
    customers = Customer.objects.all()
    return render(request, "wallet/customers_list.html",
    {"customers": customers})
