from django.contrib import admin
from .models import Customer
from .models import Wallet
from .models import Account
from .models import Transaction
from .models import Card
from .models import ThirdParty
from .models import Notification
from .models import Receipt
from .models import Loan
from .models import Reward

class CustomerAdmin(admin.ModelAdmin):
    list_display= ('first_name','last_name','age','email')
    search_fields = ('first_name','last_name')
    
admin.site.register(Customer, CustomerAdmin)
class AccountAdmin(admin.ModelAdmin):
    list_display= ('account_number','account_name','balance','pin','currency')
    search_fields = ('account_number','account_name')
class WalletAdmin(admin.ModelAdmin):
    list_display= ('balance','customer','currency','amount','account_pin')
    search_fields = ('customer','account_name')
admin.site.register(Wallet, WalletAdmin)

admin.site.register(Account, AccountAdmin)
class TransactionAdmin(admin.ModelAdmin):
    list_display= ('transaction_code','transaction_amount','transaction_type','date_time','origin_account','destination_account')
    search_fields = ('wallet','transaction_code')
admin.site.register(Transaction,TransactionAdmin)

admin.site.register(Card)
admin.site.register(ThirdParty)
admin.site.register(Notification)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)







# Register your models here.
