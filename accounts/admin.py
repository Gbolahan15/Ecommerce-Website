from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.
'''Modifying the admin dashboard to make password read only, displaying, ordering and so on...'''
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',) # show it in descending order

    filter_horizontal = ()
    list_filter = ()
    fieldsets = () 

admin.site.register(Account, AccountAdmin)

