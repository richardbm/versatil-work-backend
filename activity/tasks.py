from activity import models as activity_models
from notifications.tasks import send_email, save_notification
from celery import shared_task


@shared_task
def notify_for_response(response_id, data={}):
    # template = 'top-artist.html'
    response = activity_models.ResponseToActivity.objects.get(id=response_id)
    activity = response.activity
    subject = "Response for your demmand '%s'" % activity.title
    data['title'] = subject
    to = activity.owner.email
    #TODO Hacer template
    save_notification({}, subject, "Versatile Work", activity.owner)
    send_email(subject=subject, to=to, data=data, template=None)
