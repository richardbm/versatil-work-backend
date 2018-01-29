import graphene
from accounts.auth.facebook import auth_facebook


class AuthFacebookInput(graphene.InputObjectType):
    facebook_token = graphene.String()


class AuthenticateUserMutation(graphene.Mutation):
    class Arguments:
        facebook_token = graphene.String()

    token = graphene.String()

    @staticmethod
    def mutate(root, access_token, *args, **kwargs):
        instance = auth_facebook(web_access_token=access_token)

        return instance