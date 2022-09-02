from django.contrib import admin
from .models import Customer, Balance

# Register your models here.
class BalanceInline(admin.TabularInline):
    model = Balance
    extra = 3

class CustomerAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,
    {'fields': ['customer_text']}),
    ('Date_info',
    {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    list_display = ('customer_text', 'pub_date', 'deposited_recently')
    list_filter = ['pub_date']
    search_fields = ['customer_text']
    list_per_page = 5
    inlines = [BalanceInline]

admin.site.register(Customer, CustomerAdmin)
