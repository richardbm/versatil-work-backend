from activity.models import (Activity, ResponseToActivity,
                             OfferToActivity, DONE)
from activity.validations import (resolve_category,
                                  resolve_activity)
from accounts.models import RatingSupply


def create_activity(params):
    params['category'] = resolve_category(params)
    instance = Activity.objects.create(**params)
    return instance


def create_response(params):
    params['activity'] = resolve_activity(params)
    instance = ResponseToActivity.objects.create(**params)
    return instance


def rating_activity(params):
    activity = resolve_activity(params)
    params['activity'] = activity
    params['user'] = activity.contract.offer.owner
    params['points'] = params.pop("rating")
    instance = RatingSupply.objects.create(**params)
    activity.status = DONE
    activity.save()
    return instance


def create_offer(params):
    params['activity'] = resolve_activity(params)
    instance = OfferToActivity.objects.create(**params)
    return instance
