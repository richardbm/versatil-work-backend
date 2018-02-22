from activity import models as activity_models
from notifications.tasks import send_email, save_notification
from celery import shared_task


@shared_task
def notify_for_response(response_id, data={}):
    # template = 'top-artist.html'
    response = activity_models.ResponseToActivity.objects.get(id=response_id)
    activity = response.activity
    subject = "Respuesta para: %s" % activity.title
    data['title'] = subject
    to = activity.owner.email
    data["id"] = activity.id
    data["profile_photo"] = response.owner.facebook_picture_url
    #TODO Hacer template
    save_notification(data, subject, "Versatile Work", activity.owner)
    # send_email(subject=subject, to=to, data=data, template=None)
    # for response in activity.responses.exclude(owner=activity.owner):
    #     save_notification(data, subject, "Versatile Work", response.owner)
    #     send_email(subject=subject, to=to, data=data, template=None)



@shared_task
def notify_for_offer(response_id, data={}):
    # template = 'top-artist.html'
    offer = activity_models.OfferToActivity.objects.get(id=response_id)
    activity = offer.activity
    subject = "Nueva oferta para: %s" % activity.title
    data['title'] = subject
    to = activity.owner.email
    data["id"] = activity.id
    data["profile_photo"] = offer.owner.facebook_picture_url
    #TODO Hacer template
    save_notification(data, subject, "Versatile Work", activity.owner)
    # send_email(subject=subject, to=to, data=data, template=None)
    # for offer in activity.responses.exclude(owner=activity.owner):
    #     save_notification(data, subject, "Versatile Work", offer.owner)
    #     send_email(subject=subject, to=to, data=data, template=None)
