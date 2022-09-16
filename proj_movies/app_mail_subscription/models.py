from django.db import models


class MailSubscription(models.Model):
    email = models.EmailField('Почта')
    time_create = models.DateTimeField('Дата запроса', auto_now_add=True)

    def __str__(self):
         return f'{self.email}'

    class Meta:
        verbose_name = 'Подписка на рассылку'
        verbose_name_plural = 'Подписки на рассылку'
