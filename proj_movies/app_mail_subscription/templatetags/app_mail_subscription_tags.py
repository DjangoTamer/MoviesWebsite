from django import template
from app_mail_subscription.models import MailSubscription
from app_mail_subscription.forms import MailSubscriptionForm

register = template.Library()

@register.inclusion_tag('tags/mail_subscription.html')
def mail_subscription_form():
    return {'form': MailSubscriptionForm}
