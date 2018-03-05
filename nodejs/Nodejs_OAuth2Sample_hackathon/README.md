## Node.js OAuth2 Getting started for hackathon

The [Intuit Developer team](https://developer.intuit.com) has written this OAuth 2.0 Sample App in Node.js for beginners only to get started with QBO API. 

### Configure and Run your app

1. Clone this repo
2. ```cd``` into Node_OAuth2sample_hackathon folder
3. Open quickbooks_simple.js and enter the access token and realmId you got from [OAuth2 Playground](https://developer.intuit.com/v2/ui#/playground)
4. From terminal, enter ```npm install``` and then ```npm start```
5. From any browser go to [http://localhost:3002/getCall](http://localhost:3002/getCall) and [http://localhost:3002/postCall](http://localhost:3002/postCall) to see API response

### Sample details

quickbooks_simple.js has two demo functions
1. Get company info call
2. Create customer in QBO company

### Other resources:
1. Check out the [3rd party library](https://github.com/mcohen01/node-quickbooks) for faster development
2. Check out [another sample app](https://github.com/IntuitDeveloper/oauth2-nodejs) to implement OAuth2
3. [Other Node.js samples](https://github.com/IntuitDeveloper?utf8=%E2%9C%93&q=node&type=&language=)
