import graphene
from accounts import views as accounts_views
from accounts import models as accounts_models
from activity import views as activity_views
from activity import models as activity_models
from notifications import views as notifications_views
from notifications import models as notifications_models
from utils.graphql.pagination import paginate
from accounts import mutations as accounts_mutations
from activity import mutations as activity_mutations


class Query(graphene.ObjectType):
    users = graphene.List(accounts_views.User, id=graphene.ID())
    me = graphene.Field(accounts_views.User)
    logged_in_user = graphene.Field(accounts_views.LoggedInUser)
    activity = graphene.List(activity_views.ActivityType,
                             type_activity=graphene.String(),
                             limit=graphene.Int(),
                             offset=graphene.Int(),
                             new=graphene.Boolean())
    notifications = graphene.List(notifications_views.NotificationType,
                             limit=graphene.Int(),
                             offset=graphene.Int(),
                             new=graphene.Boolean())

    def resolve_users(self, info, **kwargs):
        return accounts_models.User.objects.all()

    def resolve_me(self, info, **kwargs):
        #TODO obtener por session
        return accounts_models.User.objects.first()

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

    def resolve_notifications(self, info, **kwargs):
        #TODO filtrar por owner
        notification = notifications_models.Notification.objects.all()
        notification = notification.select_related("owner").order_by("-date")
        notification = paginate(notification, kwargs)
        return notification


class MyMutations(graphene.ObjectType):
    authenticate_user = accounts_mutations.AuthenticateUserMutation.Field()
    create_activity = activity_mutations.CreateActivityMutation.Field()
    response_activity = activity_mutations.ResponseActivityMutation.Field()


schema = graphene.Schema(query=Query, mutation=MyMutations)

