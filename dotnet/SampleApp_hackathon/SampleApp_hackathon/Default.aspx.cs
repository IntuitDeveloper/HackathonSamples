using System;
using System.Collections.Generic;
using System.Net;
using System.Configuration;
using Intuit.Ipp.OAuth2PlatformClient;
using Intuit.Ipp.Exception;
using Intuit.Ipp.Core;
using Intuit.Ipp.Data;
using System.Threading.Tasks;
using System.Reflection;
using System.Web.Configuration;

namespace SampleApp_hackathon
{
    public partial class Default : System.Web.UI.Page
    {
        static string discoveryUrl = ConfigurationManager.AppSettings["discoveryUrl"];
        static string clientID = ConfigurationManager.AppSettings["clientID"];
        static string clientSecret = ConfigurationManager.AppSettings["clientSecret"];
        static string realmId = ConfigurationManager.AppSettings["realmId"];
        static string accessToken = ConfigurationManager.AppSettings["accessToken"];
        static string refreshToken = ConfigurationManager.AppSettings["refreshToken"];
        static string logPath = ConfigurationManager.AppSettings["logPath"];
        static string discoveryAuth = ConfigurationManager.AppSettings["DiscoveryAuthority"];

        public static Dictionary<string, string> dictionary = new Dictionary<string, string>();

        protected void Page_PreInit(object sender, EventArgs e)
        {
                dictionary.Add("clientId", clientID);
                dictionary.Add("clientSecret", clientSecret);
                dictionary.Add("accessToken", accessToken);
                dictionary.Add("refreshToken", refreshToken);
                dictionary.Add("realmId", realmId);
        }
        protected async void Page_Load(object sender, EventArgs e)
        {
            this.AsyncMode = true;
            String customerCreate = await CreateCustomerApiCall();
            createCustomerLabel.Visible = true;
            createCustomerLabel.Text = "Customer created with Id: " + customerCreate + ". Please put a break point in Page_load method to debug and see API response.";

            String companyInfo = await GetCompanyInfoApiCall();
            companyInfoLabel.Visible = true;
            companyInfoLabel.Text = "Company Info: " + companyInfo + ". Please put a break point in Page_load method to debug and see API response.";
        }

        #region qbo calls
        /// <summary>
        /// Calls create customer and checks for 401 UnAuthorized error
        /// </summary>
        /// <returns>customer Id</returns>
        public async Task<String> CreateCustomerApiCall()
        {
            try
            {  
                output("Making QBO API Call.");
                Helper.InitializeContext initialize = new Helper.InitializeContext(dictionary["accessToken"], dictionary["refreshToken"], dictionary["realmId"]);
                ServiceContext servicecontext = initialize.InitializeQBOServiceContextUsingoAuth();
                Customer customer = QBOApp.CreateCustomer(servicecontext);
                return customer.Id;
            }
            catch (IdsException ex)
            {
                if (ex.Message == "Unauthorized-401")
                {
                    output("Invalid/Expired Access Token.");
                    //if you get a 401 token expiry then perform token refresh
                    TokenResponse refreshAccessTokenResponse = await Helper.OAuth2Helper.refreshAccessToken(refreshToken, clientID, clientSecret, discoveryUrl);

                    if (refreshAccessTokenResponse.HttpStatusCode == HttpStatusCode.OK)
                    {
                        //save the refresh token in persistent store so that it can be used to refresh short lived access tokens
                        refreshToken = refreshAccessTokenResponse.RefreshToken;
                        if (!dictionary.ContainsKey("refreshToken"))
                        {
                            dictionary.Add("refreshToken", refreshToken);
                        }
                        else
                        {
                            dictionary["refreshToken"] = refreshToken;
                        }

                        output("Refresh token obtained.");

                        accessToken = refreshAccessTokenResponse.AccessToken;

                        output("Access token obtained.");
                        if (!dictionary.ContainsKey("accessToken"))
                        {
                            dictionary.Add("accessToken", accessToken);
                        }
                        else
                        {
                            dictionary["accessToken"] = accessToken;
                        }
                    }
                    
                    if ((dictionary.ContainsKey("accessToken")) && (dictionary.ContainsKey("refreshToken")) && (dictionary.ContainsKey("realmId")))
                    {
                        // update data store with new access and refresh token values

                        Helper.InitializeContext initialize = new Helper.InitializeContext(dictionary["accessToken"], dictionary["refreshToken"], dictionary["realmId"]);
                        ServiceContext servicecontext = initialize.InitializeQBOServiceContextUsingoAuth();

                        Customer customer = QBOApp.CreateCustomer(servicecontext);
                        return customer.Id;
                    }
                    return "Cannot make refresh access token API call";
                }
                else
                {
                    output(ex.Message);
                    return ex.Message;
                }
            }

        }

        /// <summary>
        /// Calls get companyInfo method and checks for 401 UnAuthorized error
        /// </summary>
        /// <returns>companyInfo Id</returns>
        public async Task<String> GetCompanyInfoApiCall()
        {
            try
            {
                output("Making QBO API Call.");
                Helper.InitializeContext initialize = new Helper.InitializeContext(dictionary["accessToken"], dictionary["refreshToken"], dictionary["realmId"]);
                ServiceContext servicecontext = initialize.InitializeQBOServiceContextUsingoAuth();
                CompanyInfo company = QBOApp.GetCompanyInfo(servicecontext);
                return company.Id;
            }
            catch (IdsException ex)
            {
                if (ex.Message == "Unauthorized-401")
                {
                    output("Invalid/Expired Access Token.");
                    //if you get a 401 token expiry then perform token refresh
                    TokenResponse refreshAccessTokenResponse = await Helper.OAuth2Helper.refreshAccessToken(refreshToken, clientID, clientSecret, discoveryUrl);

                    if (refreshAccessTokenResponse.HttpStatusCode == HttpStatusCode.OK)
                    {
                        //save the refresh token in persistent store so that it can be used to refresh short lived access tokens
                        refreshToken = refreshAccessTokenResponse.RefreshToken;
                        if (!dictionary.ContainsKey("refreshToken"))
                        {
                            dictionary.Add("refreshToken", refreshToken);
                        }
                        else
                        {
                            dictionary["refreshToken"] = refreshToken;
                        }

                        output("Refresh token obtained.");

                        accessToken = refreshAccessTokenResponse.AccessToken;

                        output("Access token obtained.");
                        if (!dictionary.ContainsKey("accessToken"))
                        {
                            dictionary.Add("accessToken", accessToken);
                        }
                        else
                        {
                            dictionary["accessToken"] = accessToken;
                        }
                    }

                    if ((dictionary.ContainsKey("accessToken")) && (dictionary.ContainsKey("refreshToken")) && (dictionary.ContainsKey("realmId")))
                    {
                        // update data store with new access and refresh token values

                        Helper.InitializeContext initialize = new Helper.InitializeContext(dictionary["accessToken"], dictionary["refreshToken"], dictionary["realmId"]);
                        ServiceContext servicecontext = initialize.InitializeQBOServiceContextUsingoAuth();

                        CompanyInfo company = QBOApp.GetCompanyInfo(servicecontext);
                        return company.Id;
                    }
                    return "Cannot make refresh access token API call";
                }
                else
                {
                    output(ex.Message);
                    return ex.Message;
                }
            }

        }

        #endregion

        # region Logging helper methods
        /// <summary>
        /// Gets the log path
        /// </summary>
        /// <returns></returns>
        public string GetLogPath()
        {
            try
            {
                if (logPath == "")
                {
                    logPath = System.Environment.GetEnvironmentVariable("TEMP");
                    if (!logPath.EndsWith("\\")) logPath += "\\";
                }
            }
            catch
            {
                output("Log error path not found.");
            }
            return logPath;
        }

        /// <summary>
        /// Appends the given string to the on-screen log, and the debug console.
        /// </summary>
        /// <returns></returns>
        public void output(string logMsg)
        {
            //Console.WriteLine(logMsg);

            System.IO.StreamWriter sw = System.IO.File.AppendText(GetLogPath() + "OAuth2SampleAppLogs.txt");
            try
            {
                string logLine = System.String.Format(
                    "{0:G}: {1}.", System.DateTime.Now, logMsg);
                sw.WriteLine(logLine);
            }
            finally
            {
                sw.Close();
            }
        }

        #endregion 
    }
}