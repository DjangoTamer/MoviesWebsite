from django.views.generic import CreateView
from app_mail_subscription.models import MailSubscription
from app_mail_subscription.forms import MailSubscriptionForm

class MailSubscriptionView(CreateView):
    model = MailSubscription
    form_class = MailSubscriptionForm
    success_url = "/"

