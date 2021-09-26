from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Deposit, Balance, Material
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class DepositInline(admin.StackedInline):
    model = Deposit
    max_num = 1

class DepositsUserAdmin(UserAdmin):
    inlines = [DepositInline]


@register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    pass
@register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    pass

@register(Material)
class MaterialAdmin(admin.ModelAdmin):
    pass

# unregister old user admin
admin.site.unregister(User)
# register new user admin that includes a UserProfile
admin.site.register(User, DepositsUserAdmin)