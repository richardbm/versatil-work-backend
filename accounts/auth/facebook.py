from django.conf import settings
import requests
import json
from accounts import models as accounts_models
from django.utils.translation import ugettext_lazy as _


def auth_facebook(web_access_token):

    # obtener nuevo access_token
    params = {
        'client_id': settings.FACEBOOK_CLIENT,
        'redirect_uri': settings.REDIRECT_URI,
        'client_secret': settings.FACEBOOK_SECRET,
        'code': web_access_token
    }

    r = requests.get(settings.ACCESS_TOKEN_URL, params=params)
    try:
        access_token = json.loads(r.text)
    except Exception as e:
        raise Exception(_("error comunicationg with Facebook: %s" % str(e)))

    var_access_token = access_token.get("access_token", None)
    if var_access_token is None:
        raise Exception(_("error comunicationg with Facebook: %s" % str(r.text)))

    params = {
        'client_id': settings.FACEBOOK_CLIENT,
        'grant_type': "fb_exchange_token",
        'client_secret': settings.FACEBOOK_SECRET,
        'fb_exchange_token': var_access_token
    }

    # obtener datos de perfil
    r = requests.get(settings.ACCESS_TOKEN_URL, params=params)
    access_token = json.loads(r.text)
    r = requests.get(settings.GRAPH_API_URL, params=access_token)
    profile = json.loads(r.text)
    user = accounts_models.User.objects.filter(facebook_id=profile["id"]).first()

    if not user:
        user = create_user_from_facebook(profile, user)

    if user.is_active is False:
        raise Exception(_("Your account has been disabled."))

    token, created = accounts_models.Token.objects.get_or_create(user=user)
    data = create_login_data(token, user)
    return data['token']


def create_login_data(token, user):
    return {
        'registered': True,
        'token': token.key,
        'user': {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "facebook_picture_url": user.facebook_picture_url,
            "hometown": user.hometown
        }
    }


def create_user_from_facebook(profile, user):
    user = accounts_models.User()
    user.facebook_id = profile["id"]
    user.username = profile["id"]
    user.first_name = profile["first_name"]
    user.last_name = profile["last_name"]
    user.hometown = profile["hometown"]["name"] if "hometown" in profile.keys() else ""
    user.email = profile["email"] if 'email' in profile else str(profile['id'] + '@facebook.com')
    user.save()
    return user
