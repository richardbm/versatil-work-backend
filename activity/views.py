from graphene_django_extras import DjangoObjectType
from activity import models as activity_models
from utils.models import Image
from contracts.models import Contract
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


class ResponseType(DjangoObjectType):

    class Meta:
        model = activity_models.ResponseToActivity
        description = " Type definition for Responses"


class OfferType(DjangoObjectType):

    class Meta:
        model = activity_models.OfferToActivity
        description = " Type definition for Offers"


class ContractsType(DjangoObjectType):
    class Meta:
        model = Contract
        description = " Type definition for a activity's contract"


class ActivityType(DjangoObjectType):
    image = graphene.List(ImageType)
    type_activity_display = graphene.String()
    first_image = graphene.String()
    responses = graphene.List(ResponseType)
    offers = graphene.List(OfferType)
    contract = graphene.Field(ContractsType)

    def resolve_first_image(self, *args, **kwargs):
        images = self.image.all()
        if images:
            return images[0].image.url
        return None

    def resolve_type_activity_display(self, *args, **kwargs):
        return self.get_type_activity_display()

    def resolve_image(self, *args, **kwargs):
        return self.image.all()

    def resolve_contract(self, *args, **kwargs):
        contract = Contract.objects.filter(activity__id=self.id).first()
        return contract

    def resolve_responses(self, *args, **kwargs):
        return self.responses.all().order_by("date")

    def resolve_offers(self, *args, **kwargs):
        if self.status == activity_models.OPEN:
            return self.offers.all().order_by("-date")
        return [self.contract.offer]

    class Meta:
        model = activity_models.Activity
        description = " Type definition for a single activity "
