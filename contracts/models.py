from django.db import models


class Contract(models.Model):
    activity = models.OneToOneField("activity.Activity",
                                    related_name="contract",
                                    on_delete=models.CASCADE)
    offer = models.ForeignKey("activity.OfferToActivity",
                              on_delete=models.CASCADE)
    scheduled_for = models.DateTimeField()
    date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.activity.title
