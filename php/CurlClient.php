<?php
/*******************************************************************************
 * Copyright (c) 2017 Intuit
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *  http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *******************************************************************************/
require ("./BaseCurl.php");
/**
 * Class CurlHttpClient
 *
 * A Http Client using PHP cURL extension to send HTTP/HTTPS request to QuickBooks Online
 *
 *
 */
class CurlClient  {

    /**
    * @var BaseCurl The basecURL instance will be used for performing Http/Https client request.
    */
    private $basecURL = null;

    /**
    * @var IntuitResponse | False The parsed response from curl client to Intuit customized response
    */
    private $intuitResponse = false;

    /**
     * Status code
     */
    private $httpStatusCode;

    private $headers;

    private $bodies;
    /**
     * The constructor for constructing the cURL http client for making API calls
     * @param BaseCurl $curl    A predefined BaseCurl instance to be used in this client
     */
    public function __construct(BaseCurl $curl = null)
    {
        if(isset($curl)){
              $this->basecURL = $curl;
        }else{
              $this->basecURL = new BaseCurl();
        }
    }

    /**
     * @inheritdoc
     */
    public function makeAPICall($url, $method, array $headers, $body, $timeOut, $verifySSL){
        $this->prepareRequest($url, $method, $headers, $body, $timeOut, $verifySSL);
        $rawResponse = $this->executeRequest();
        $this->handleErrors();
        $this->intuitResponse = $rawResponse;
        $this->setIntuitResponseHeader($rawResponse);
        $this->setIntuitResponseCode($rawResponse);
        $this->setIntuitResponseBody($rawResponse);
        $this->closeConnection();
        return $this->getLastResponse();
    }

    /**
     * @inheritdoc
     */
    public function prepareRequest($url, $method, array $headers, $body, $timeOut, $verifySSL){
        //Set basic Curl Info
        $curl_opt = [
            CURLOPT_URL => $url,
            CURLOPT_CUSTOMREQUEST => trim($method),
            //Set return transfer to true so the curl_exec will return the result
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $this->getHeaders($headers),
            //10 seconds is allowed to make the connection to the server
            CURLOPT_CONNECTTIMEOUT => 10,
            CURLOPT_TIMEOUT => isset($timeOut) ? $timeOut : 100,
            CURLOPT_RETURNTRANSFER => true,
            //When CURLOPT_HEADER is set to 0 the only effect is that header info from the response is excluded from the output.
            //So if you don't need it that's a few less KBs that curl will return to you.
            //In our case, header is required
            CURLOPT_HEADER => true
        ];

        if ($method !== "GET" && isset($body)) {
          $curl_opt[CURLOPT_POSTFIELDS] = $body;
        }

        $this->intializeCurl();
        $this->basecURL->setupCurlOptArray($curl_opt);
    }

    /**
     * Send a request and return the response
     * @return curlResponse
     */
    private function executeRequest(){
        return $this->basecURL->execute();
    }

    /**
     * The error during HTTP/HTTPS call. For example, the certificate expired. The server respond time out. It has nothing to do with the
     * status code returned from server.
     */
    private function handleErrors(){
        if($this->basecURL->errno() || $this->basecURL->error()){
           $errorMsg = $this->basecURL->error();
           $errorNumber = $this->basecURL->errno();
           throw new \Exception("cURL error during making API call. cURL Error Number:[" . $errorNumber . "] with error:[" . $errorMsg . "]");
        }
    }

    /**
     * Check if the cURL instance exists. If not or closed, create a new BaseCurl instance for this Http client
     */
    private function intializeCurl(){
        if($this->basecURL->isCurlSet()){ return; }
        else {$this->basecURL->init();}
    }

    /**
    * Get headers for the QuciKbooks Online Response
    */
    private function getHeaders($headers){
      if(!isset($headers) || empty($headers)){
          throw new \Exception("Error. The headers set for cURL are either NULL or Empty");
      }else{
          $convertedHeaders = $this->convertHeaderArrayToHeaders($headers);
          return $convertedHeaders;
      }
    }

    /**
     * Convert an Array to Curl Headers
     * @param array $headerArray The request headers
     * @return Curl Array Headers
     */
    public function convertHeaderArrayToHeaders(array $headerArray){
         $headers = array();
         foreach($headerArray as $k => $v){
              $headers[] = $k . ":" . $v;
         }
         return $headers;
    }

    /**
     * close the connection of current http client
     */
    private function closeConnection(){
        $this->basecURL->close();
    }

    /**
     * @inheritdoc
     */
    public function getLastResponse(){
        return $this->intuitResponse;
    }

    private function setIntuitResponseHeader($response){
        $headerSize = $this->basecURL->getInfo(CURLINFO_HEADER_SIZE);
        $rawHeaders = mb_substr($response, 0, $headerSize);
        $this->headers = $rawHeaders;
    }

    private function setIntuitResponseCode($response){
        $httpStatusCode = $this->basecURL->getInfo(CURLINFO_HTTP_CODE);
        $this->httpStatusCode = $httpStatusCode;
    }

    private function setIntuitResponseBody($response){
       $headerSize = $this->basecURL->getInfo(CURLINFO_HEADER_SIZE);
       $rawHeaders = mb_substr($response, 0, $headerSize);
       $rawBody = mb_substr($response, $headerSize);
       $this->bodies = $rawBody;
    }

    /**
     * Get status Code
     * @return Integer
     */
    public function getLastStatusCode(){
        return $this->httpStatusCode;
    }

    /**
     * Get response Header
     * @return String
     */
    public function getLastHeader(){
        return $this->headers;
    }

    /**
     * Get response Body
     * @return String
     */
    public function getLastBody(){
        return $this->bodies;
    }


}

 ?>
