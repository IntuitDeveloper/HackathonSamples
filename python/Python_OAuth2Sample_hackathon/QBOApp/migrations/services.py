from django.conf import settings
from datetime import datetime
import urllib
import requests
import base64
import json
import random
from jose import jws, jwk
from base64 import urlsafe_b64decode, b64decode

def refreshAccessToken(refreshToken):
	token_endpoint = getDiscoveryDocument.token_endpoint
    auth_header = 'Basic ' + stringToBase64(settings.CLIENT_ID + ':' + settings.CLIENT_SECRET)
    headers = {'Accept': 'application/json', 'content-type': 'application/x-www-form-urlencoded', 'Authorization' : auth_header}
    payload = {
    'refresh_token': refresh_Token,
    'grant_type': 'refresh_token'
    }
    r = requests.post(token_endpoint, data=payload, headers=headers)
    bearer_raw = json.loads(r.text)

    if 'id_token' in bearer_raw:
        idToken = idToken=bearer_raw['id_token']
    else:
        idToken = None
    
    return Bearer(bearer_raw['x_refresh_token_expires_in'],bearer_raw['access_token'],bearer_raw['token_type'], bearer_raw['refresh_token'], bearer_raw['expires_in'], idToken=idToken)


def getDiscoveryDocument(discoveryDocUrl):
	# 	

