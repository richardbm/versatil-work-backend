from celery import shared_task
from django.conf import settings
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string
from pyfcm import FCMNotification
from . import models
EMAIL_TEMPLATE_DEFAULT = "email-template-default.html"


@shared_task
def send_email(subject, to, data={}, template=None):
    data["url"] = settings.URL
    from_email = settings.EMAIL_HOST_USER
    if not template:
        template = EMAIL_TEMPLATE_DEFAULT
    text_content = render_to_string(template, data)
    html_content = render_to_string(template, data)
    send = EmailMultiAlternatives(subject, text_content, from_email, [to])
    send.attach_alternative(html_content, "text/html")
    send.send()
    return True

#
# @shared_task
# def send_push(data, registration_ids, msg_push, user):
#     push_service = FCMNotification(api_key=settings.API_KEY)
#     message_title = "Versatile Work"
#     message_body = msg_push
#     notification = save_notification(data, message_body, message_title, user)
#     data["notification_id"] = notification.id
#     push_service.notify_multiple_devices(registration_ids=registration_ids,
#                                          message_title=message_title,
#                                          message_body=message_body,
#                                          data_message=data)


def save_notification(data={}, message_body="", message_title="", user=None):
    notification = models.Notification()
    notification.owner = user
    notification.title = message_title
    notification.body = message_body
    if data:
        notification.data = data
    notification.save()
    return notification


def serializer_data(data):
    data_result = {}
    for key in data.keys():
        value = data.get(key)
        if isinstance(value, str) or isinstance(value, int):
            data_result[key] = value
    return data_result


def get_all_fcm(user):
    registration_ids = user.fcm_device.all()
    registration_ids = [obj.registration_id for obj in registration_ids]
    return registration_ids


# EXAMPLE TASK
#
# @shared_task
# def send_artist_stats_email(subject, to, data={}):
#     template = 'artist-stats.html'
#     return send_email(subject=subject, to=to, data=data, template=template)
#
# @shared_task
# def send_top_ten_artist_email(subject, to, data={}):
#     template = 'top-artist.html'
#     data['title'] = "Ranking Global"
#     return send_email(subject=subject, to=to, data=data, template=template)
