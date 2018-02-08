# Java Sample App using SDK

The [Intuit Developer team](https://developer.intuit.com) has written this OAuth 2.0 Sample App in Java to provide working examples how to use Java SDK to make QBO API calls using tokens generated from the [OAuth Playground](https://developer.intuit.com/v2/ui#/playground) 

## Table of Contents

* [Requirements](#requirements)
* [First Use Instructions](#first-use-instructions)
* [Running the code](#running-the-code)
* [Storing the Tokens](#storing-the-tokens)


## Requirements

In order to successfully run this sample app you need a few things:

1. Java 1.8
2. A [developer.intuit.com](http://developer.intuit.com) account
3. An app on [developer.intuit.com](http://developer.intuit.com) and the associated client id and client secret.
 
## First Use Instructions

1. Clone the GitHub repo to your computer
2. Fill in the [`application.properties`](src/main/resources/application.properties) file values (OAuth2AppClientId, OAuth2AppClientSecret) by copying over from the keys section for your app.
3. Use the [Oauth playground](https://developer.intuit.com/v2/ui#/playground) to generate tokens and ill in the [`application.properties`](src/main/resources/application.properties) file values (accessToken, refreshToken, companyid).

## Running the code

Once the sample app code is on your computer, you can do the following steps to run the app:

1. cd to the project directory</li>
2. Run the command:`./gradlew bootRun` (Mac OS) or `gradlew.bat bootRun` (Windows)</li>
3. Wait until the terminal output displays the "Started Application in xxx seconds" message.
4. Your app should be up now in http://localhost:8080/ 


The sample app demonstrates the following flows:

**QBO CompanyInfo GET API** - this flow shows how to make a QBO API Get request using SDK to fetch Company Information.

**QBO Create Customer POST API** - this flow shows how to make a QBO API Post request using SDK to create a customer.

**Handle expired tokens** - Both the API calls above demonstrates how to refresh the token when token expires.


## Storing the tokens
This app stores all the tokens and user information in the session. For production ready app, tokens should be encrypted and stored in a database.
