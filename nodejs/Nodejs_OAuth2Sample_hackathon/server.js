const express = require ('express');
var session = require('express-session');
//const debug = require('debug')('expressdebug:server')
const QBORequests = require('./QBORequests');
const OAuth2Helper = require('./OAuth2Helper');
const config = require('./config');
const app = express();
const request = require('request');

app.use(session({
	resave: false,
    saveUninitialized: true,
	secret: 'secret',
}))

app.use(function (req, res, next) {
  if (!req.session.accessToken) {
    req.session.accessToken = config.AccessToken
  }
  if (!req.session.refreshToken) {
    req.session.refreshToken = config.RefreshToken
  }
  if (!req.session.realmId) {
    req.session.realmId = config.RealmId
  }
  next()
})

app.get('/', function(req, resp){
	resp.send('Route to /getCall and /postCall to see result');
})

app.get('/getCall', function(req, resp){

	QBORequests.getCompanyInfo(req.session.accessToken, req.session.realmId, function(apiResponse) {
		if(JSON.parse(apiResponse.statusCode) === 401) {
			OAuth2Helper.refreshAccessToken(req.session.refreshToken, function(tokenResp){
				if(tokenResp != null) {
					req.session.refreshToken = tokenResp.refresh_token;
					req.session.accessToken = tokenResp.access_token;
					QBORequests.getCompanyInfo(req.session.accessToken, req.session.realmId, function(apiResponseRetry) {	
						console.log('After 401: ' + JSON.stringify(apiResponseRetry.body));
						resp.send(JSON.stringify(apiResponseRetry.body));
					});
				}
				else {
					console.log('Refreshing access token failure.');
				}
			});
		}
		else if(JSON.parse(apiResponse.statusCode) === 200) {
			console.log('Successful response '+ JSON.stringify(apiResponse.body));
			resp.send(JSON.stringify(apiResponse.body));
		}
		else {
			console.log('Something went wrong. Here\'s the full response: ' + JSON.stringify(apiResponse));
			resp.send(JSON.stringify(apiResponse.body));
		}

	});
})

app.get('/postCall', function(req, resp){
	QBORequests.createCustomer(req.session.accessToken, req.session.realmId, function(apiResponse) {
		if(JSON.parse(apiResponse.statusCode) === 401) {
			OAuth2Helper.refreshAccessToken(req.session.refreshToken, function(tokenResp){
				if(tokenResp != null) {
					req.session.refreshToken = tokenResp.refresh_token;
					req.session.accessToken = tokenResp.access_token;
					QBORequests.createCustomer(req.session.accessToken, req.session.realmId, function(apiResponseRetry) {	
						console.log('After 401: ' + JSON.stringify(apiResponseRetry.body));
						resp.send(JSON.stringify(apiResponseRetry.body));
					});
				}
				else {
					console.log('Refreshing access token failure.');
				}
			});
		}
		else if(JSON.parse(apiResponse.statusCode) === 200) {
			console.log('Successful response '+ JSON.stringify(apiResponse.body));
			resp.send(JSON.stringify(apiResponse.body));
		}
		else {
			console.log('Something went wrong. Here\'s the full response: ' + JSON.stringify(apiResponse));
			resp.send(JSON.stringify(apiResponse.body));
		}

	});
})

app.listen(3002, () => {
    console.log('Running Express.js on port 3002.');
});
