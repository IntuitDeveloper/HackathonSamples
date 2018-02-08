const express = require ('express');
const axios = require('axios');


const app = express();

app.get('/', function(req,resp){
  const quickbooks_sandbox_baseurl = 'https://sandbox-quickbooks.api.intuit.com';
  const url = quickbooks_sandbox_baseurl + '/v3/company/193514538214074/companyinfo/193514538214074';
	const config = {
		headers: {
					'Accept': 'application/json',
					'Content-Type': 'application/json',
					'Authorization': 'Bearer eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..4TQwFBnbjoC8p9rz1CH52Q.wchk72SkwV0HTsOVO_c-oQYbC1EXcSed31DeJklcpnZ7-wGZ5IDeSKvlJZHdKvJB2t6OHOY_ZA7wck4Zbk40t4Z_UDp27J28kbA0KC-HacEN--pr2qiY7WlFKtBcrnYGpxDTUIA_cMDRu065Yy2vs8ebMiYqSy4ezZPpnb6hwlMqeF05Q6PLcMQC5xrto29M9yPKP9tJcRt4d7HM4AVED4dNG9-WnZEYk2cB2VXATxRENpFpWtee-eoy68e2WcLFlxX6xs6Odpuy2pN50mXOb5hzvmbSVc9zopSz4q0I0e_UQmLuXbvI2K_Skg1VTjI-CeWeHZo-3FlDtDyrsmPbo1lWh9S0F66r29F2JjES8v4UfxLlz457kRwTwXgmIiq2gxtJh52SV3Iqa9ST9EzD7510FCxp4FUIOTVgyL9_ZWSI8Y3O01g7HNwUtkd1pntZslvkVMLxlc8nI5COSENAmv_9kHfuxmTPYBw1F7LF-BTgBLGKBn_tYbFP37KgX0TosPIwwu0VGaA8QMyS_rVZdqo28wbcVfrjtcuNHsrEgWALljptsTVzbPuWfTT7WDQgtDaKXkoD-z40gHciMJg4nUCebbW6LiZmjA3aeHGV4b8h8R_UKb97C1PFtOUBEKP8Y_hVF5yWVP_okHvUWD4oEZWkcOP650s1PUYD9pKv9clz_7bvHrdvIcBeTErwhHD_.duhOr6TnD5XwNOqA2KPiSw'
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
    axios.get(url, config).then( function (response) {
      resp.send(JSON.stringify(response.data));
	  }).catch(function (error) {
    	console.log(error);
	  });
})

app.listen(3000, () => {
    console.log('Running Express.js on port 3000.');
});
