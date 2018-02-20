# PHP Sample Create Invoice

The [Intuit Developer team](https://developer.intuit.com) has written this OAuth 2.0 Sample App in PHP to provide working examples on how to make QBO API calls to create an Invoice using tokens generated from the [OAuth Playground](https://developer.intuit.com/v2/ui#/playground)

## Table of Contents

* [Requirements](#requirements)
* [First Use Instructions](#first-use-instructions)
* [Running the code](#running-the-code)


## Requirements

In order to successfully run this sample app you need a few things:

1. PHP 5.4 or above, with Curl extension installed
2. A [developer.intuit.com](http://developer.intuit.com) account
3. An app on [developer.intuit.com](http://developer.intuit.com) 

## First Use Instructions

1. Clone the GitHub repo to your computer
2. Use the [Oauth playground](https://developer.intuit.com/v2/ui#/playground) to generate OAuth 2 tokens
3. Provide your Access Token and RealmID from playground, and environment(sandbox/production) in the [`SampleInvoiceCreateAPICall.php`](https://github.com/IntuitDeveloper/HackathonSamples/blob/master/php/SampleInvoiceCreateAPICall.php) file $settings array


## Running the code

Once the sample app code is on your computer, you can do the following steps to run the app:

php SampleInvoiceCreateAPICall.php


