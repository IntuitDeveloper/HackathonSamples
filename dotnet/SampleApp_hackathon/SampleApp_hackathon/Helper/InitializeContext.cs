using System;
using Intuit.Ipp.Security;
using Intuit.Ipp.Core;

namespace SampleApp_hackathon.Helper
{
    public class InitializeContext
    {
        public string accessToken { get; set; }
        public string refreshToken { get; set; }
        public string realmId { get; set; }

        public InitializeContext()
        {
        }
        public InitializeContext(string accessToken, string refreshToken, string realmId)
        {
            this.accessToken = accessToken;
            this.refreshToken = refreshToken;
            this.realmId = realmId;
        }

        public ServiceContext InitializeQBOServiceContextUsingoAuth()
        {
            //Initialize();
            OAuth2RequestValidator reqValidator = new OAuth2RequestValidator(this.accessToken);
            ServiceContext context = new ServiceContext(this.realmId, IntuitServicesType.QBO, reqValidator);

            //MinorVersion represents the latest features/fields in the xsd supported by the QBO apis.
            //Read more details here- https://developer.intuit.com/docs/0100_quickbooks_online/0200_dev_guides/accounting/querying_data

            context.IppConfiguration.MinorVersion.Qbo = "12";
            return context;
        }
    }
}