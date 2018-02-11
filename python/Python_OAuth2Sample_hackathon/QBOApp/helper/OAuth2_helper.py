"""
    Refresh Access Token helper module
"""
import json
import base64
import requests

def refresh_access_token(config):
    """
        Refreshed OAuth2 access token in case access token expired
    """
    discovery_doc = requests.get(config['discovery_doc']).json()
    token_endpoint = discovery_doc['token_endpoint']

    encoded = _string_to_base64(config['client_id'] + ':' + config['client_secret'])
    auth_header = 'Basic ' + encoded
    
    headers =   {
                    'Accept': 'application/json', 
                    'content-type': 'application/x-www-form-urlencoded', 
                    'Authorization' : auth_header
                }
    
    payload =   {
                    'refresh_token': config['refresh_token'],
                    'grant_type': 'refresh_token'
                }
    
    r = requests.post(token_endpoint, headers=headers, data=payload)
    print('Refresh Token Call')
    print (r.content)
    return r.json()

def _string_to_base64(my_str):
    """
        Encodes string to base64
    """
    return base64.b64encode(bytes(my_str, 'utf-8')).decode()
