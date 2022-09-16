from django.contrib import admin
from app_mail_subscription.models import MailSubscription

@admin.register(MailSubscription)
class MailSubscriptionAdmin(admin.ModelAdmin):
   list_display = ('email', 'time_create')

