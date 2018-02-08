const axios = require('axios');

const quickbooks_sandbox_baseurl = 'https://sandbox-quickbooks.api.intuit.com';
const quickbooks_production_baseurl = 'https://quickbooks.api.intuit.com';

/* 
	Get OAuth2 access token from OAuth2 playground: 
	https://developer.intuit.com/v2/ui#/playground
	== OR ==
	Go to app's dashboard, click on Test connect to app and get access token and realm id
*/

const oauth2_access_token = '<EnterOAuth2AccessTokenHere>';
const realm_id = '<EnterRealmIdHere>';

/*
	If you're getting 401, please go to OAuth2 playground and get new access token 
*/

function get_company_info(access_token, realmId) {
	const url = quickbooks_sandbox_baseurl + '/v3/company/' + realmId + '/companyinfo/' + realmId + '?minorversion=12';
	const config = {
		headers: {
					'Accept': 'application/json',
					'Content-Type': 'application/json',
					'Authorization': 'Bearer '+ access_token
		}
	}

	axios.get(url, config).then( function (response) {
		console.log(response.status);
		console.log(response.headers);
		console.log(JSON.stringify(response.data));
	}).catch(function (error) {
    	console.log(error);
	});
}

get_company_info (oauth2_access_token, realm_id);


function create_customer(access_token, realmId) {
	const url = quickbooks_sandbox_baseurl + '/v3/company/'+realmId+'/customer?minorversion=12';
	const config = {
		headers: {
					'Accept': 'application/json',
					'Content-Type': 'application/json',
					'Authorization': 'Bearer '+ access_token
		}
	}

	// Refer to Customer and other enitity documentation here: https://developer.intuit.com/docs/api/accounting/customer
	const body = {
				    "BillAddr": {
				        "Line1": "123 Main Street",
				        "City": "Mountain View",
				        "Country": "USA",
				        "CountrySubDivisionCode": "CA",
				        "PostalCode": "94042"
				    },
				    "Notes": "Here are other details.",
				    "DisplayName": "King's Groceries1",
				    "PrimaryPhone": {
				        "FreeFormNumber": "(555) 555-5555"
				    },
				    "PrimaryEmailAddr": {
				        "Address": "jdrew@myemail.com"
				    }
				};

	axios.post(url, body, config).then( function (response) {
		console.log(response.status);
		console.log(response.headers);
		console.log(JSON.stringify(response.data));
	}).catch(function (error) {
    	console.log(error);
	});
}

create_customer (oauth2_access_token, realm_id);