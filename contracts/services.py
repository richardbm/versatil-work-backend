from activity.validations import (resolve_activity, resolve_offer)
from contracts.models import Contract
from django.db import transaction
from activity import models as activity_models


def create_contract(params):
    with transaction.atomic():
        activity = resolve_activity(params)
        activity.status = activity_models.PENDING
        activity.save()
        params['activity'] = activity
        offer = resolve_offer(params)
        params['offer'] = offer
        params['scheduled_for'] = offer.scheduled_for
        instance = Contract.objects.create(**params)

    return instance
