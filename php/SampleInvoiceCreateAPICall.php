<?php
require ("./CurlClient.php");

$settings = [
  //Enter your access Token from OAuth 2 Playground
  "AccessToken" => "eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..JZkJdvYxyM7qcALbcnwrsQ.J2xFYA1ddmAiw7--j2qVzoyKvU8DB3DZN_fd98LyB2APDFnmkMmtn8HXmiH9LI8CB9eKE_0afx9UKjJ2qpg1zrZe-1rx14nd5Pf92TGnkbbxem3g_2-Q7jfzbIlCKIqE7J0IyI4-dFHplYYvyftmxntfhxfoJeGFAPIPKBP2pCK3V9pubkCHqSs0gKls19w6RzfQvySAi4LOyaGZsogEtYgDZAuMLbt2-55fKGt7A_y3uQUl9EYq4crYVxaY8uPZM7HbMH7WwheYi4tcrssGzetTWA7KToHVWLjuJvQ4EIS5VS4zs4_30IoM4Eu2G9LpyfT8PFYt7FbEMMmJbDC2MkpPt3yaUyi_2Vbg0Db_uM-059eGDqjAlZkbnAhtvC90xC83B9OfQE9mn3KmyXOlgm36rxZ8KLfCNjTa-U8PMGY1kL3Efg2fy1MhPNIV90USAKGDoIvGP8Jq_YAMS0VLBiw9nxPMAJFszMrMQLPcsx2Tx_lwlj0JBUMG0xG0WNkuLAdEHzfGUrSAMfzYcZL6W-UzjnqPnXMZJD4ifTLW0gQNfba5nwfyZCQEgXs0P6C7O0XExY8oaFsklx_29qz7YAb1rjDckmne31yjfVZzB3o6YiTvYels9bskEin1HyOYyBjpSgt8b9c6j2C2Bf0eLxie_hgnZc6c19YIHb2CfLGmo5QObmWqQ_tsY7EZycj1.2mhnP7dZSKcDwLUiQZ7qSw",
  //If you are using Production Keys, use "Production" here
  "Envionment" => "Development",
  "RealmID" => "193514611894164"
];

if(strcasecmp($settings["Envionment"], "Development") == 0){
    $baseURL = "https://sandbox-quickbooks.api.intuit.com/v3/company/";
}else{
    $baseURL = "https://quickbooks.api.intuit.com/v3/company/";
}

$completeURL = $baseURL . $settings["RealmID"] . "/invoice";

$CurlHttpClient = new CurlClient();

$http_header = array(
      'Accept' => 'application/json',
      'Authorization' => "Bearer " . $settings["AccessToken"],
      'Content-Type' => 'application/json'
);

$createInvoiceBody = [
   "Line" => [
     [
       "Amount" => 100.00,
       "DetailType" => "SalesItemLineDetail",
       "SalesItemLineDetail" => [
          "ItemRef" => [
              "value" => "1",
              "name" => "Services"
          ]
       ]
     ]
   ],
   "CustomerRef" => [
      "value" => "1"
   ]
];

$postBody = json_encode($createInvoiceBody);

//All response, code, header and body are in String format
$intuitResponse = $CurlHttpClient->makeAPICall($completeURL, "POST", $http_header, $postBody, null, false);
$code = $CurlHttpClient->getLastStatusCode();
$header = $CurlHttpClient->getLastHeader();
$body = $CurlHttpClient->getLastBody();

var_dump($code);
var_dump($header);
var_dump($body);
 ?>
