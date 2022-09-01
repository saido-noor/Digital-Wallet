from datetime import datetime
from locale import currency
from django.db import models
# from sqlalchemy import BigInteger, null, true

class Customer(models.Model):
    first_name= models.CharField(max_length=20 )
    last_name= models.CharField(max_length=20)
    address=models.TextField()
    email= models.EmailField()
    phone_number= models.CharField(max_length=15)
    gender= models.CharField(max_length=10)
    nationality=models.CharField(null=True,max_length=24)
    # profile_picture=models.ImageField(null=True,blank=True,upload_to="images/")
    age= models.PositiveBigIntegerField()





class Account(models.Model):
    account_number = models.IntegerField()
    account_name = models.CharField(max_length=20)
    balance = models.BigIntegerField()
    pin = models.PositiveIntegerField()
    currency = models.CharField(max_length=20)
    # wallet = models.ForeignKey()






# Create your models here.

class Wallet(models.Model):
    balance = models.BigIntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    currency = models.CharField(max_length=20)
    amount = models.BigIntegerField()
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    account_pin = models.PositiveIntegerField()



class Transaction(models.Model):
    transaction_code = models.IntegerField()
    wallet = models.ForeignKey(on_delete=models.CASCADE,to=Wallet)
    transaction_amount = models.BigIntegerField()
    transaction_type =  models.CharField(max_length=20)
    date_time = models.DateTimeField(default=datetime.now)
    origin_account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="account_a")
    destination_account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="accountb")


class Card(models.Model):
    card_account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="account_e")
    card_number = models.IntegerField()
    card_holder_name = models.CharField(max_length=39)
    wallet = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="account_f")
    expiry_date = models.DateTimeField(default=datetime.now)
    date_issued = models.DateTimeField(default=datetime.now)
    card_type = models.CharField(max_length=20)

class ThirdParty(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="account_c")
    account_number = models.BigIntegerField()
    transaction_cost = models.BigIntegerField()
    currency = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="account_d")

class Receipt(models.Model):
    receipt_type = models.CharField(max_length=20)
    receipt_date =  models.DateTimeField()
    receipt_number = models.BigIntegerField()
    total_amount = models.IntegerField()
    transaction = models.ForeignKey(on_delete=models.CASCADE,to=Transaction)
    receipt_file = models.FileField()


class Notification(models.Model):
    message = models.CharField(max_length=30)
    tittle = models.CharField(max_length=20)
    date_time = models.DateTimeField()
    recipient = models.ForeignKey(on_delete=models.CASCADE,to=Receipt)
    state = (
        ('a', 'active'),
        ('in','inactive')

    )
    status = models.CharField( max_length=10,choices=state, null=True)





class Loan(models.Model):
    amount = models.BigIntegerField()
    loan_type = models.CharField(max_length=20)
    interest_rate = models.PositiveIntegerField()
    date_time = models.DateTimeField(default=datetime.now)
    loan_id = models.SmallIntegerField()
    wallet = models.ForeignKey(on_delete=models.CASCADE,to=Wallet)
    # guarantor =  models.ForeignKey()


class Reward(models.Model):
    receipt = models.ForeignKey(Receipt,on_delete=models.CASCADE)
    transacation = models.ForeignKey(Transaction,on_delete=models.CASCADE)
    customer_id = models.IntegerField()
    date_reward = models.DateTimeField()

 