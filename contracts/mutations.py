import graphene
from activity.views import ActivityType
from contracts.views import ContractType
from contracts.services import create_contract
from contracts.tasks import notify_for_contract


class CreateContractMutation(graphene.Mutation):

    class Arguments:
        activity_id = graphene.Int(required=True)
        offer_id = graphene.Int(required=True)

    activity = graphene.Field(ActivityType)
    offer = graphene.Field(ContractType)

    @staticmethod
    def mutate(root, info, *args, **kwargs):
        instance = create_contract(kwargs)
        notify_for_contract(instance.id)
        return instance
