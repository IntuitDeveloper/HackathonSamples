# .Net Sample App using SDK

The [Intuit Developer team](https://developer.intuit.com) has written this OAuth 2.0 Sample App using .Net framework and C# to provide working examples how to use .Net SDK to make QBO API calls using tokens generated from the [OAuth Playground](https://developer.intuit.com/v2/ui#/playground) 

## Table of Contents

* [Requirements](#requirements)
* [First Use Instructions](#first-use-instructions)
* [Running the code](#running-the-code)
* [Storing the Tokens](#storing-the-tokens)


## Requirements

In order to successfully run this sample app you need a few things:

1. .Net framework 4.6.1
2. A [developer.intuit.com](http://developer.intuit.com) account
3. An app on [developer.intuit.com](http://developer.intuit.com) and the associated client id and client secret.
 
## First Use Instructions

1. Clone the GitHub repo to your computer
2. Fill in the [`Web.config`](SampleApp_hackathon/Web.config) file values (clientId, clientSecret) by copying over from the keys section for your app.
3. Use the [Oauth playground](https://developer.intuit.com/v2/ui#/playground) to generate tokens and fill values accessToken, refreshToken, realmId in the[`Web.config`](SampleApp_hackathon/Web.config) along with valid logPath for logging.

## Running the code

Once the sample app code is on your computer, you can do the following steps to run the app:

1. Open the solution in Visual Studio. This app was developed and tested on VS2017.
2. Put a breakpoint in Page_Load method to see the full API response.
3. Run the application 

The sample app demonstrates the following flows:

**QBO CompanyInfo GET API** - this flow shows how to make a QBO API Get request using SDK to fetch Company Information.

**QBO Create Customer POST API** - this flow shows how to make a QBO API Post request using SDK to create a customer.

**Handle expired tokens** - Both the API calls above demonstrates how to refresh the token when token expires.


## Storing the tokens
This app stores all the tokens and user information in the session. For production ready app, tokens should be encrypted and stored in a database. 
