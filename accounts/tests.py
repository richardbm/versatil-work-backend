from django.test import TestCase
from versatilwork.schema import schema
from model_mommy import mommy


class MockerUSer:
    def __init__(self, user):
        self.user = user

    def is_authenticated(self):
        return True


class TestAccounts(TestCase):
    def test_query_me(self):
        user = mommy.make("accounts.user")
        query = '''
            query currentUser {
                me {
                    id
                    firstName
                    lastName
                    facebookPictureUrl
                    ratingSupply
                }
            }
        '''
        result = schema.execute(query, context_value=MockerUSer(user))
        self.assertFalse(result.errors, result.errors)

    def test_query_user(self):
        user = mommy.make("accounts.user")
        query = '''
            query detailUser {
                user(id:"%s") {
                    id
                    firstName
                    lastName
                    facebookPictureUrl
                    ratingSupply
                }
            }
        ''' % user.id
        result = schema.execute(query, context_value=MockerUSer(user))
        self.assertFalse(result.errors, result.errors)

    def test_create_supply(self):
        user = mommy.make("accounts.user")
        category = mommy.make("activity.Category")
        query = '''
        mutation CreateSupplyMutation {
            createActivity(title:"title",description:"$description",categoryId:%d,typeActivity:"SU") {
                id
                title
                description
                category {
                    id
                    name
                }
                typeActivity
            }
        }
        ''' % category.id
        result = schema.execute(query, context_value=MockerUSer(user))
        self.assertFalse(result.errors, result.errors)

    def test_create_demand(self):
        user = mommy.make("accounts.user")
        category = mommy.make("activity.Category")
        query = '''
        mutation CreateDemandMutation {
            createActivity(title:"title",description:"$description",categoryId:%d,typeActivity:"DE") {
                id
                title
                description
                category {
                    id
                    name
                }
                typeActivity
            }
        }
        ''' % category.id
        result = schema.execute(query, context_value=MockerUSer(user))
        self.assertFalse(result.errors, result.errors)
