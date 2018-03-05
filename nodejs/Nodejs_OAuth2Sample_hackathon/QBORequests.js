const request = require('request');
const uuidV4 = require('uuid/v4');
const config = require('./config');
/*
	QBO API GET Request - CompanyInfo 
*/
const getCompanyInfo = (accessToken, realmId, callback) => {
	const url = config.AccountingBaseUrl + '/v3/company/' + realmId + '/companyinfo/' + realmId + '?minorversion=' + config.MinorVersion;

	const headers = {
					'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': 'Bearer '+ accessToken
	}

	const options = {
		url: url,
		method: 'GET',
		headers: headers
	}

	request(options, function (error, response, body) {
		callback(response);
	});
}

/*
	QBO API POST Request - Create Customer 
*/
const createCustomer = (accessToken, realmId, callback) => {
	const url = config.AccountingBaseUrl + '/v3/company/' + realmId + '/customer?minorversion=' + config.MinorVersion;
	const headers = {
					'Accept': 'application/json',
					'Content-Type': 'application/json',
					'Authorization': 'Bearer '+ accessToken
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
					"GivenName": "Katie" + uuidV4(),
					"FamilyName": "McLaren",
				    "PrimaryPhone": {
				        "FreeFormNumber": "(555) 555-5555"
				    },
				    "PrimaryEmailAddr": {
				        "Address": "jdrew@myemail.com"
				    }
				}

	const options = {
		url: url,
		method: 'POST',
		headers: headers,
		json: body
	}

	request(options, function (error, response, body) {
		callback(response);
	});
	
};

module.exports = {
	getCompanyInfo,
	createCustomer,
};
