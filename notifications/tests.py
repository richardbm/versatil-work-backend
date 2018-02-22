from django.test import TestCase
from versatilwork.schema import schema
from model_mommy import mommy


class MockerUSer:
    def __init__(self, user):
        self.user = user

    def is_authenticated(self):
        return True


class TestNotifications(TestCase):
    def test_query_notifications(self):
        user = mommy.make("accounts.user")
        mommy.make("notifications.Notification", owner=user,_quantity=10)
        query = '''
            query NotificationsQuery {
                notifications {
                    id
                    body
                    date
                    data
                }
            }
        '''
        result = schema.execute(query, context_value=MockerUSer(user))
        self.assertFalse(result.errors, result.errors)
