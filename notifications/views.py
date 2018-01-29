from graphene_django_extras import DjangoObjectType, DjangoListObjectType
from notifications import models as notifications_models


class NotificationType(DjangoObjectType):

    class Meta:
        model = notifications_models.Notification
        description = " Type definition for a notifications about the activity"
