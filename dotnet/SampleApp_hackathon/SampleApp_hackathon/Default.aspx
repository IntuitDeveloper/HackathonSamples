<%@ Page Async="true" Language="C#" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="SampleApp_hackathon.Default" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <p >This sample app demonstrates a simple QBO GET(CompanyInfo) and POST(Create a vendor) call. Add app's Client Id, Client Secret along with Access Token, Refresh Token, Realm Id (you can get these from OAuth playground from app's dashboard) and a valid physical path for logging in the config file to run this application. <p>

            <br /><br /><br />

            <p>POST API request - Create a customer</p>
            <asp:label runat="server" id="createCustomerLabel" visible="false">"Created customer payload here.</asp:label>

            <br /><br /><br />

            <p>GET API request - Get Company Info</p>
            <asp:label runat="server" id="companyInfoLabel" visible="false">"Created customer payload here.</asp:label>

        </div>
    </form>
</body>
</html>
