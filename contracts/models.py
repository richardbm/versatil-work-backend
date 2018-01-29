from django.db import models


class Contract(models.Model):
    activity = models.OneToOneField("activity.Activity",
                                    on_delete=models.CASCADE)
    response = models.OneToOneField("activity.ResponseToActivity",
                                    on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.activity.title
