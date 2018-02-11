"""
    Views module
"""
import os
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template
from .QBO_requests import create_bill, get_bill
from .helper import OAuth2_helper

# Create your views here.
def index(request):
    '''Index view of application does a POST and a GET API request'''
    read_config(request)
    config = {}
    for key, value in request.session.items():
        config[key] = value

    create_bill_status, create_bill_response = create_bill(config)

    # If HTTP status code 401 is returned by the API, getting a fresh access token is required since access tokens are valid only for 60 min.
    if create_bill_status == 401:
        fresh_tokens = OAuth2_helper.refresh_access_token(config)
        if fresh_tokens:
            update_session(request, fresh_tokens['access_token'], fresh_tokens['refresh_token'])
        else:
            return HttpResponse('Could not refresh access token.')

        # Update config with the right tokens
        config['access_token'] = request.session['access_token']
        config['refresh_token'] = request.session['refresh_token']

        # Make API requests with fresh acces token
        create_bill_status, create_bill_response = create_bill(config)
    
    get_bill_status, get_bill_response = get_bill(config, create_bill_response["Bill"]["Id"])

    # If HTTP status code 401 is returned by the API, getting a fresh access token is required since access tokens are valid only for 60 min.
    if get_bill_status == 401:
        fresh_tokens = OAuth2_helper.refresh_access_token(config)
        if fresh_tokens:
            update_session(request, fresh_tokens['access_tokens'], fresh_tokens['refresh_tokens'])
        else:
            return HttpResponse('Could not refresh access token.')

        # Update config with the right tokens
        config['access_token'] = request.session['access_token']
        config['refresh_token'] = request.session['refresh_token']

        # Make API requests with fresh acces token        
        get_bill_status, get_bill_response = get_bill(config, create_bill_response["Bill"]["Id"])
    context = {
            'post_request': create_bill_response,
            'get_request': get_bill_response,
        }
    return render(request, 'index.html', context=context)

def update_session(request, access_token, refresh_token):
    '''Update session with fresh tokens and then write new values to config.json
        This is just for demo purposes. Actual refresh token with realm Id will be saved in database while access token in session.
    '''
    request.session['access_token'] = access_token
    request.session['refresh_token'] = refresh_token
    config = {}
    for key, value in request.session.items():
        config[key] = value
    file_path = os.path.abspath(os.path.join(__file__ , '../../config.json'))
    with open(file_path, 'w') as f:
        json.dump(config, f)
    f.close()

def read_config(request):
    '''Read config values from config.json and load them in session'''    
    file_path = os.path.abspath(os.path.join(__file__ , '../../config.json'))
    with open(file_path, 'r') as f:
        config = json.load(f)
    f.close()
    request.session['access_token'] = config['access_token']
    request.session['refresh_token'] = config['refresh_token']
    request.session['realm_id'] = config['realm_id']
    request.session['qbo_base_url'] = config['qbo_base_url']
    request.session['client_id'] = config['client_id']
    request.session['client_secret'] = config['client_secret']
    request.session['discovery_doc'] = config['discovery_doc']
