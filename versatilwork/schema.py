import graphene
from accounts import views as accounts_views
from accounts import models as accounts_models
from activity import views as activity_views
from activity import models as activity_models
from utils.graphql.pagination import paginate


class Query(graphene.ObjectType):
    users = graphene.List(accounts_views.User, id=graphene.ID())
    activity = graphene.List(activity_views.ActivityType,
                             type_activity=graphene.String(),
                             limit=graphene.Int(),
                             offset=graphene.Int())

    def resolve_users(self, info, **kwargs):
        return accounts_models.User.objects.all()

    def resolve_activity(self, info, **kwargs):
        type_activity = kwargs.get("type_activity")
        activity_model = activity_models.Activity.objects
        if type_activity and type_activity != "ALL":
            activity = activity_model.filter(type_activity=type_activity)
        else:
            activity = activity_model.all()
        activity = activity.select_related("owner")
        activity = activity.prefetch_related("category", "image").order_by("-date")
        activity = paginate(activity, kwargs)
        return activity


schema = graphene.Schema(query=Query)

