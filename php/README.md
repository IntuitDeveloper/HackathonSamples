# PHP Sample Create Invoice

The [Intuit Developer team](https://developer.intuit.com) has written this OAuth 2.0 Sample App in PHP to provide working examples on how to make QBO API calls to create an Invoice using tokens generated from the [OAuth Playground](https://developer.intuit.com/v2/ui#/playground)

## Table of Contents

* [Requirements](#requirements)
* [First Use Instructions](#first-use-instructions)
* [Running the code](#running-the-code)
* [Storing the Tokens](#storing-the-tokens)


## Requirements

In order to successfully run this sample app you need a few things:

1. PHP 5.4 or above
2. A [developer.intuit.com](http://developer.intuit.com) account
3. An app on [developer.intuit.com](http://developer.intuit.com) and the associated client id and client secret.

## First Use Instructions

1. Clone the GitHub repo to your computer
2. Provide your Access Token, RealmID, and environment(sandbox/production) in the [`SampleInvoiceCreateAPICall`](src/main/resources/application.properties) file $settings array


## Running the code

Once the sample app code is on your computer, you can do the following steps to run the app:

php SampleInvoiceCreateAPICall.php


The sample app demonstrates the following flows:

**QBO CompanyInfo GET API** - this flow shows how to make a QBO API Get request using SDK to fetch Company Information.

**QBO Create Customer POST API** - this flow shows how to make a QBO API Post request using SDK to create a customer.

**Handle expired tokens** - Both the API calls above demonstrates how to refresh the token when token expires.


## Storing the tokens
This app stores all the tokens and user information in the session. For production ready app, tokens should be encrypted and stored in a database.
