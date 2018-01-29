from django.db import models
from django.contrib.postgres.fields import JSONField


class FCMDevice(models.Model):
    registration_id = models.TextField()
    user = models.ForeignKey('accounts.User',
                             on_delete=models.CASCADE,
                             related_name='fcm_device')

    def __str__(self):
        return self.user.email

    class Meta:
        unique_together = ('user', 'registration_id',)


class Notification(models.Model):
    title = models.TextField()
    body = models.TextField()
    data = JSONField(blank=True, null=True)
    owner = models.ForeignKey('accounts.User',
                              on_delete=models.CASCADE,
                              related_name='notifications')
    read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.email
