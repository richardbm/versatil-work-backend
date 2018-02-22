from django.test import TestCase
from versatilwork.schema import schema
from model_mommy import mommy


class MockerUSer:

    def __init__(self, user):
        self.user = user

    @staticmethod
    def is_authenticated(self):
        return True


class TestActivity(TestCase):

    def test_query_activity(self):
        user = mommy.make("accounts.user")
        category = mommy.make("activity.category")
        mommy.make("activity.Activity", owner=user, category=category)
        query = '''
            query ActivityQuery {
                activity {
                    id
                    title
                    description
                    typeActivity
                    date
                    status
                    typeActivityDisplay
                    owner {
                        id
                        firstName
                        lastName
                    }
                    category {
                        icon
                        iconColor
                        backgroundColor
                    }
        
                }
            }
        '''
        result = schema.execute(query, context_value=MockerUSer(user))
        self.assertFalse(result.errors, result.errors)

    def test_query_detail_activity(self):
        user = mommy.make("accounts.user")
        category = mommy.make("activity.category")
        activity = mommy.make("activity.Activity", owner=user, category=category)
        query = '''
        query ActivityQuery {
            detailActivity(id: %d) {
                id
                title
                description
                firstImage
                typeActivity
                date
                status
                typeActivityDisplay
                contract {
                    offer {
                        owner {
                            id  
                        }
                    }
                }
                offers {
                    id
                    price
                    scheduledFor
                    description
                    owner {
                        id
                        firstName
                        lastName
                        facebookPictureUrl
    
                    }
    
                }
                responses {
                    id
                    description
                    date
                    owner {
                        id
                        firstName
                        lastName
                        facebookPictureUrl
                        
                    }
                }
                owner {
                    id
                    firstName
                    lastName
                    phone
                }
                category {
                    icon
                    iconColor
                    backgroundColor
                }
    
            }
        }
        ''' % activity.id
        result = schema.execute(query, context_value=MockerUSer(user))
        self.assertFalse(result.errors, result.errors)

    def test_query_calendar(self):
        user = mommy.make("accounts.user")
        category = mommy.make("activity.category")
        activity = mommy.make("activity.Activity", status="PE", owner=user, category=category)
        offer = mommy.make("activity.OfferToActivity", activity=activity, owner=user)
        mommy.make("contracts.Contract", activity=activity, offer=offer)
        query = '''
            query Query {
                activity(status: "PE"){
                    id
                    title
                    description
                    firstImage
                    typeActivity
                    date
                    typeActivityDisplay
                    owner {
                        id
                        firstName
                        lastName    
                    }
                    category {
                        icon
                        iconColor
                        backgroundColor
                    }
        
                }
            }
        '''
        result = schema.execute(query, context_value=MockerUSer(user))
        self.assertFalse(result.errors, result.errors)

    def test_add_offer_to_activity(self):
        user = mommy.make("accounts.user")
        category = mommy.make("activity.category")
        activity = mommy.make("activity.Activity", owner=user, category=category)
        query = '''
            mutation OfferActivityMutation {
                offerActivity(description:"$description",activityId:%d,price:"123",scheduledFor:"2018-02-09T00:00:00Z") {
                    id
                    description
                    activity {
                        id
                    }
                    owner {
                        id
                        firstName
                        lastName
                        phone
                    }
                }
            }
        ''' % activity.id
        result = schema.execute(query, context_value=MockerUSer(user))
        self.assertFalse(result.errors, result.errors)

    def test_add_comment_to_activity(self):
        user = mommy.make("accounts.user")
        category = mommy.make("activity.category")
        activity = mommy.make("activity.Activity", owner=user, category=category)
        query = '''
            mutation ResponseActivityMutation {
                responseActivity(description:"$description",activityId:%d) {
                    id
                    description
                    activity {
                        id
                    }
                    owner {
                        id
                        firstName
                        lastName
                        phone
                    }
                }
            }
        ''' % activity.id
        result = schema.execute(query, context_value=MockerUSer(user))
        self.assertFalse(result.errors, result.errors)
