from django.contrib import admin

from order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('car', 'email', 'name', 'created_at', 'closed', 'email_sent',)
    list_filter = ('car', )
