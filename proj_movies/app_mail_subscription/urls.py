from django.urls import path
from app_mail_subscription.views import MailSubscriptionView

urlpatterns = [
    path('', MailSubscriptionView.as_view(), name='mail_subscription'),
    ]