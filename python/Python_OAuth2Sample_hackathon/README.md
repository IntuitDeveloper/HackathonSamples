# Python Sample App using Django

The [Intuit Developer team](https://developer.intuit.com) has written this OAuth 2.0 Sample App in Python 3 to provide working examples of how to make QBO API calls using tokens generated from the [OAuth Playground](https://developer.intuit.com/v2/ui#/playground) 

## Table of Contents

* [Requirements](#requirements)
* [First Use Instructions](#first-use-instructions)
* [Running the code](#running-the-code)
* [Storing the Tokens](#storing-the-tokens)


## Requirements

In order to successfully run this sample app you need a few things:

1. Python 3 and Django framework
2. A [developer.intuit.com](http://developer.intuit.com) account
3. An app on [developer.intuit.com](http://developer.intuit.com) and the associated client id and client secret.
 
## First Use Instructions

1. Clone the GitHub repo to your computer
2. Use the [Oauth playground](https://developer.intuit.com/v2/ui#/playground) to generate tokens 
3. Fill in the [`config.json`](config.json) file values file values (access_token, refresh_token, realm_id, client_id, client_secret).

## Running the code

Once the sample app code is on your computer, you can do the following steps to run the app:

1. cd to the project directory</li>
2. Run the command:`python manage.py runserver` (Mac OS) </li>
3. Wait until the terminal output displays the "Starting development server at http://127.0.0.1:8000/" message.
4. Your app should be up now in http://localhost:8000/QBOApp 


The sample app demonstrates the following:

**QBO Create Bill POST API** [`QBO_requests.py`](QBOApp/QBO_requests.py) - Shows how to make a QBO API Post request to create a customer.

**QBO Bill GET API** [`QBO_requests.py`](QBOApp/QBO_requests.py) - Shows how to make a QBO API Get request using the above created Bill Id to read it.

**Handle expired tokens** [`OAuth2_helper.py`](QBOApp/helper/OAuth2_helper.py) - Demonstrates how to refresh the token when token expires.

**Supporting QBO API requests** [`QBO_helper.py`](QBOApp/helper/QBO_helper.py) - Shows how to create supporting entities like Item, Vendor and Account

## Storing the tokens
This app stores all the tokens and user information in the session and config file. For production ready app, tokens should be encrypted and stored in a database.
