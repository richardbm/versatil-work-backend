from graphene_django_extras import DjangoObjectType
from accounts import models as accounts_models
import graphene


class User(DjangoObjectType):
    class Meta:
        model = accounts_models.User
        description = " Type definition for a single user "
        filter_fields = {'id': ['iexact']}


class LoggedInUser(DjangoObjectType):
    id = graphene.Int()

    class Meta:
        model = accounts_models.User
        description = " Type definition for a single user "
        filter_fields = {'id': ['iexact']}

