from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import *
from django.contrib.auth.models import User


@receiver(post_save, sender=Response)
def new_response_notify(sender, instance, created, **kwargs):
    if created:
        for user in User.objects.all():
            if user == instance.resp_post.author.authorUser:
                html_content = render_to_string(
                    'notification.html',
                    {
                        'instance': instance,
                        'username': user.username,
                    }
                )
                msg = EmailMultiAlternatives(
                    subject=f'New response to ad {instance.resp_post}',
                    body=f'{instance.text}',
                    from_email='ayr215215@yandex.ru',
                    to=[f'{user.email}'],
                )
                msg.attach_alternative(html_content, "text/html")

                msg.send()
    else:
        for user in User.objects.all():
            if user == instance.resp_user:
                html_content = render_to_string(
                    'response_accepted.html',
                    {
                        'instance': instance,
                    }
                )

                msg = EmailMultiAlternatives(
                    subject=f'Your response to post {instance.resp_post} was accepted',
                    body=instance.text,
                    from_email='ayr215215@yandex.ru',
                    to=[f'{instance.from_user.email} '],
                )
                msg.attach_alternative(html_content, "text/html")  # добавляем html

                msg.send()
