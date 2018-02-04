import graphene
from accounts import views as accounts_views
from accounts import models as accounts_models
from activity import views as activity_views
from activity import models as activity_models
from notifications import views as notifications_views
from notifications import models as notifications_models
from utils.graphql.pagination import paginate
from accounts import mutations as accounts_mutations
from django.db.models import Q
from activity import mutations as activity_mutations


class Query(graphene.ObjectType):
    users = graphene.List(accounts_views.User, id=graphene.ID())
    me = graphene.Field(accounts_views.User)
    logged_in_user = graphene.Field(accounts_views.LoggedInUser)
    category = graphene.List(activity_views.CategoryType)
    activity = graphene.List(activity_views.ActivityType,
                             type_activity=graphene.String(),
                             limit=graphene.Int(),
                             offset=graphene.Int(),
                             status=graphene.String(),
                             new=graphene.Boolean())
    detail_activity = graphene.Field(activity_views.ActivityType,
                                     id=graphene.ID())
    notifications = graphene.List(notifications_views.NotificationType,
                                  limit=graphene.Int(),
                                  offset=graphene.Int(),
                                  new=graphene.Boolean())

    def resolve_users(self, info, **kwargs):
        return accounts_models.User.objects.all()

    def resolve_category(self, info, **kwargs):
        return activity_models.Category.objects.all()

    def resolve_me(self, info, **kwargs):
        user = info.context.user
        if not user.is_authenticated:
            return None
        return user

    def resolve_detail_activity(self, info, **kwargs):
        activity_id = kwargs.get("id")
        activity = activity_models.Activity.objects.get(id=activity_id)
        return activity

    def resolve_activity(self, info, **kwargs):
        type_activity = kwargs.get("type_activity")
        status = kwargs.get("status", activity_models.OPEN)
        activity_model = activity_models.Activity.objects
        activity = activity_model.filter(status=status)
        # if status == activity_models.PENDING:
        #     user = info.context.user
        #     activity = activity_model.filter(Q(owner=user)
        #                                      | Q(contract__ofer__owner=user))
        if type_activity and type_activity != "ALL":
            activity = activity.filter(type_activity=type_activity)
        activity = activity.select_related("owner")
        activity = activity.prefetch_related("category", "image").order_by("-date")
        activity = paginate(activity, kwargs)
        return activity

    def resolve_notifications(self, info, **kwargs):
        user = info.context.user
        notification = notifications_models.Notification.objects.filter(owner=user)
        notification = notification.select_related("owner").order_by("-date")
        notification = paginate(notification, kwargs)
        return notification


class MyMutations(graphene.ObjectType):
    authenticate_user = accounts_mutations.AuthenticateUserMutation.Field()
    create_activity = activity_mutations.CreateActivityMutation.Field()
    response_activity = activity_mutations.ResponseActivityMutation.Field()


schema = graphene.Schema(query=Query, mutation=MyMutations)

