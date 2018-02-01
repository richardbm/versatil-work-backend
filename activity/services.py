from activity.models import Activity, ResponseToActivity
from activity.validations import (resolve_category,
                                  resolve_activity)


def create_activity(params):
    params['category'] = resolve_category(params)
    instance = Activity.objects.create(**params)
    return instance


def create_response(params):
    params['activity'] = resolve_activity(params)
    instance = ResponseToActivity.objects.create(**params)
    return instance
