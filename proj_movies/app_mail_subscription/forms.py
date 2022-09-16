from django import forms
from app_mail_subscription.models import MailSubscription
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class MailSubscriptionForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = MailSubscription
        fields = ('email', 'captcha')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'editContent', 'placeholder': "Enter your email..."}),
        }
        labels = {
            'email': ''
        }
