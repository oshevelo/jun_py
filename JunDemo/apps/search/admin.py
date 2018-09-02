from django.contrib import admin
from apps.search.models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'external_id']
    list_per_page = 50
