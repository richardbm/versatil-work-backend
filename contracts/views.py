import graphene
from graphene_django import DjangoObjectType
from activity.views import OfferType, ActivityType
from contracts.models import Contract


class ContractType(DjangoObjectType):
    offers = graphene.Field(OfferType)
    activity = graphene.Field(ActivityType)

    class Meta:
        model = Contract
        description = " Type definition for Contracts"
