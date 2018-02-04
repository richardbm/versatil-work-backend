from django.db import models
from django.utils.translation import ugettext_lazy as _

SUPPLY = "SU"
DEMAND = "DE"
ACTIVITY_TYPE = (
    (SUPPLY, _("Supply")),
    (DEMAND, _("Demand")),
)


class Category(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    icon_color = models.CharField(max_length=50)
    background_color = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


OPEN = "OP"
PENDING = "PE"
DONE = "DO"
CANCELlED = "pe"

STATUS_ACTIVITY = (
    (OPEN, _("Abierta")),
    (PENDING, _("Pendiente")),
    (DONE, _("Realizada")),
    (CANCELlED, _("Cancelada")),
)


class Activity(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ManyToManyField("utils.Image", blank=True)
    type_activity = models.CharField(max_length=2, choices=ACTIVITY_TYPE)
    owner = models.ForeignKey("accounts.User",
                              on_delete=models.SET(1))
    date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=STATUS_ACTIVITY,
                              default=OPEN)
    category = models.ForeignKey("activity.Category",
                                 on_delete=models.SET(1))

    def __str__(self):
        return self.title


class ResponseToActivity(models.Model):
    activity = models.ForeignKey("activity.Activity",
                                 on_delete=models.CASCADE,
                                 related_name="responses")
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey("accounts.User",
                              on_delete=models.SET(1))

    def __str__(self):
        return "{0} {1}".format(self.owner.get_full_name(), self.description)


class OfferToActivity(models.Model):
    activity = models.ForeignKey("activity.Activity",
                                 on_delete=models.CASCADE,
                                 related_name="offers")
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey("accounts.User",
                              on_delete=models.SET(1))

    def __str__(self):
        return "{0} {1}".format(self.owner.get_full_name(), self.description)
