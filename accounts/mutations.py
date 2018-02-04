import graphene
from accounts.auth.facebook import auth_facebook
from accounts.views import User


class AuthFacebookInput(graphene.InputObjectType):
    facebook_token = graphene.String()


class AuthenticateUserMutation(graphene.Mutation):
    class Arguments:
        facebook_token = graphene.String()

    key = graphene.String()
    user = graphene.Field(User)

    @staticmethod
    def mutate(root, *args, **kwargs):
        web_access_token = kwargs.get("facebook_token")
        instance = auth_facebook(web_access_token=web_access_token)
        return instance
