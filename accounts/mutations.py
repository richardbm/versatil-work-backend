import graphene
from accounts.auth.facebook import auth_facebook


class AuthFacebookInput(graphene.InputObjectType):
    facebook_token = graphene.String()


class AuthenticateUserMutation(graphene.Mutation):
    class Arguments:
        facebook_token = graphene.String()

    key = graphene.String()

    @staticmethod
    def mutate(root, *args, **kwargs):
        web_access_token = kwargs.get("facebook_token")
        instance = auth_facebook(web_access_token=web_access_token)
        return instance
