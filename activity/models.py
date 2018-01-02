from django.db import models
from django.utils.translation import ugettext_lazy as _

SUPPLY = "SU"
DEMAND = "DE"
ACTIVITY_TYPE = (
    (SUPPLY, _("Supply")),
    (DEMAND, _("Demand")),
)


class Category(models.Model):
    # TODO: Hacerlo con emoticons unicode
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    icon_color = models.CharField(max_length=50)
    background_color = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ManyToManyField("utils.Image", blank=True)
    type_activity = models.CharField(max_length=2, choices=ACTIVITY_TYPE)
    owner = models.ForeignKey("accounts.User",
                              on_delete=models.SET(1))
    date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey("activity.Category",
                                 on_delete=models.SET(1))

    def __str__(self):
        return self.title
