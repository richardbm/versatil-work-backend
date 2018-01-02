from graphene_django_extras import DjangoObjectType, DjangoListObjectType
from activity import models as activity_models
from utils.models import Image
import graphene


class ImageType(DjangoObjectType):
    url = graphene.String()

    def resolve_url(self, *args, **kwargs):
        return self.image.url

    class Meta:
        model = Image
        description = " Type definition for a image"


class CategoryType(DjangoObjectType):
    class Meta:
        model = activity_models.Category
        description = " Type definition for a activity's category "


class ActivityType(DjangoObjectType):
    image = graphene.List(ImageType)
    type_activity_display = graphene.String()
    first_image = graphene.String()

    def resolve_first_image(self, *args, **kwargs):
        images = self.image.all()
        if images:
            return images[0].image.url
        return None

    def resolve_type_activity_display(self, *args, **kwargs):
        return self.get_type_activity_display()

    def resolve_image(self, *args, **kwargs):
        return self.image.all()

    class Meta:
        model = activity_models.Activity
        description = " Type definition for a single activity "
