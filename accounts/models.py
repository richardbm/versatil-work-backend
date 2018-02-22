from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import signals
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
import os
import binascii


class User(AbstractUser):
    """
    the purpose of this class is to more easily
    extend the user model in the future.
    """
    phone = models.CharField(max_length=15, blank=True, null=True)
    facebook_id = models.TextField(blank=True)
    facebook_picture_url = models.URLField(blank=True, null=True)
    rating_supply = models.IntegerField(default=0)

    def __str__(self):
        return str(self.username)


class Token(models.Model):
    """
    The default authorization token model.
    """
    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='auth_token',
        on_delete=models.CASCADE, verbose_name=_("User")
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key


CHOICE_POINTS = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
)


class RatingSupply(models.Model):
    user = models.ForeignKey("User",
                             related_name="list_rating_supply",
                             on_delete=models.CASCADE)
    activity = models.ForeignKey("activity.Activity",
                                 on_delete=models.CASCADE)
    points = models.IntegerField(choices=CHOICE_POINTS)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name()


def save_rating(sender, instance, created=None, **kwargs):
    if created:
        user = instance.user
        rating_queryset = user.list_rating_supply.all()
        list_points = [obj.points for obj in rating_queryset]
        points = sum(list_points) / rating_queryset.count()
        user.rating_supply = points
        user.save()


signals.post_save.connect(save_rating, sender=RatingSupply)
