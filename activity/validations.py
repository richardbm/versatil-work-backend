from activity.models import Activity, Category, OfferToActivity
from accounts.models import User
from django.utils.translation import ugettext_lazy as _


def resolve_owner(params):
    name = "owner_id"
    param_id = params.get(name)
    return resolve_relation(User, name, param_id)


def resolve_category(params):
    name = "category_id"
    param_id = params.get(name)
    return resolve_relation(Category, name, param_id)


def resolve_activity(params):
    name = "activity_id"
    param_id = params.get(name)
    return resolve_relation(Activity, name, param_id)


def resolve_offer(params):
    name = "offer_id"
    param_id = params.get(name)
    return resolve_relation(OfferToActivity, name, param_id)


def resolve_relation(model, param_name, param_id=None, required=True):

    if not param_id:

        if required is False:
            return None
        raise Exception(_("'%s' is required" % param_name))
    instance = model.objects.filter(id=param_id).first()

    if not instance:
        raise Exception(_("%s does not exist" % model._meta.model_name))

    return instance
