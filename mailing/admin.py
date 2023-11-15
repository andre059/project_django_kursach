from django.contrib import admin

from mailing.models import Mailing, Message, Client, Logs


admin.site.register(Client)
admin.site.register(Logs)
admin.site.register(Message)
admin.site.register(Mailing)
