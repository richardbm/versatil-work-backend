from contracts.models import Contract
from notifications.tasks import send_email, save_notification
from celery import shared_task


@shared_task
def notify_for_contract(response_id, data={}):
    # template = 'top-artist.html'
    contract = Contract.objects.get(id=response_id)
    activity = contract.activity
    subject = "Tu oferta fue seleccionada en: %s" % activity.title
    data['title'] = subject
    to = contract.offer.owner.email
    data["id"] = activity.id
    data["profile_photo"] = contract.activity.owner.facebook_picture_url
    #TODO Hacer template
    save_notification(data, subject, "Versatile Work", contract.offer.owner)
    # send_email(subject=subject, to=to, data=data, template=None)
    # for contract in activity.responses.exclude(owner=activity.owner):
    #     save_notification(data, subject, "Versatile Work", contract.owner)
    #     send_email(subject=subject, to=to, data=data, template=None)

