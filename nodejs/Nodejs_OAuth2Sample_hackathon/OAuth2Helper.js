const config = require('./config');
const request = require('request');

function refreshAccessToken(refreshToken, callback){
    getTokenEndpointUrl(function(tokenEndpoint){
        if (tokenEndpoint != null){
            const headers = {
					'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': 'application/json',
                    'Authorization': 'Basic ' + require('btoa')(config.ClientId + ':' + config.ClientSecret)
		    }
	        
            const body = {
                'grant_type': 'refresh_token',
                'refresh_token': refreshToken
            }
            const options = {
                url: tokenEndpoint,
                method: 'POST',
                headers: headers,
                form: body
            }
            request(options, function (error, response, body) {
                console.log('Refrehs Token Response: ' + JSON.stringify(response));
                res = JSON.parse(body);
                if(response.statusCode === 200){
                    callback(res);
                }
                else callback(null);
            });
        }
    });
};    

function getTokenEndpointUrl(callback){
    request(config.DiscoveryUrl, function (error, response, body) {
        res = JSON.parse(body);
        if(response.statusCode == 200){
            tokenEndpoint = res.token_endpoint;
            callback(tokenEndpoint);
        }
        else callback(null);
    });
};

module.exports = {
	refreshAccessToken,
};