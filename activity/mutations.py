import graphene
from activity.services import create_activity, create_response
from accounts.views import User
from activity.views import CategoryType, ActivityType
from activity.tasks import notify_for_response


class CreateActivityMutation(graphene.Mutation):

    """
    Mutation for create activity

    e.g:

    mutation CreateActivityMutation($title:String!, $description:String!, $typeActivity:String!, $ownerId:Int!, $categoryId:Int!) {
      createActivity(title:$title, description:$description, typeActivity:$typeActivity,ownerId:$ownerId,categoryId:$categoryId) {
        title
        description
        owner {
          id
          firstName
          lastName
        }
        typeActivityDisplay
        category {
          id
          name

        }
      }
    }
    """

    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        type_activity = graphene.String(required=True)
        category_id = graphene.Int(required=True)

    id = graphene.Int()
    title = graphene.String()
    description = graphene.String()
    type_activity = graphene.String()
    type_activity_display = graphene.String()
    owner = graphene.Field(User)
    category = graphene.Field(CategoryType)

    def resolve_type_activity_display(self, *args, **kwargs):
        return self.get_type_activity_display()

    def resolve_category_display(self, *args, **kwargs):
        return self.get_category_display()

    @staticmethod
    def mutate(root, info, *args, **kwargs):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("User not auth")
        kwargs['owner'] = user
        return create_activity(kwargs)


class ResponseActivityMutation(graphene.Mutation):

    class Arguments:
        description = graphene.String(required=True)
        activity_id = graphene.Int(required=True)

    id = graphene.Int()
    activity = graphene.Field(ActivityType)
    description = graphene.String()
    owner = graphene.Field(User)

    @staticmethod
    def mutate(root, info, *args, **kwargs):
        user = info.context.user
        kwargs['owner'] = user
        instance = create_response(kwargs)
        notify_for_response(instance.id)
        return instance
