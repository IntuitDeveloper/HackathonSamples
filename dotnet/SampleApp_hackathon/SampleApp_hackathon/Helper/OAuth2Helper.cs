using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using Intuit.Ipp.OAuth2PlatformClient;
using System.Threading.Tasks;
using System.Net;
using System.Net.Http;

namespace SampleApp_hackathon.Helper
{
    public class OAuth2Helper
    {
        public static async Task<TokenResponse> refreshAccessToken(string refreshToken, string clientId, string clientSecret, string discoveryUrl) {
            DiscoveryClient client = new DiscoveryClient(discoveryUrl);
            DiscoveryResponse doc = await client.GetAsync();
            String tokenEndpoint = "";
            if (doc.StatusCode == HttpStatusCode.OK)
            {
                tokenEndpoint = doc.TokenEndpoint;
            }
            var tokenClient = new TokenClient(tokenEndpoint, clientId, clientSecret);
            TokenResponse refereshtokenCallResponse = await tokenClient.RequestRefreshTokenAsync(refreshToken);
            return refereshtokenCallResponse;
        }
    }
}