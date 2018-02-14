using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using Intuit.Ipp.Data;
using Intuit.Ipp.Core;
using Intuit.Ipp.QueryFilter;
using Intuit.Ipp.DataService;

namespace SampleApp_hackathon
{
    public class QBOApp
    {
        public static Customer CreateCustomer(ServiceContext context)
        {
            Customer customer = new Customer
            {
                GivenName = "Kaley_" + Guid.NewGuid().ToString("N"),
                FamilyName = "McMohan",
                DisplayName = "Kaley_" + Guid.NewGuid().ToString("N")+" McMohan",
                Taxable = true,
                TaxableSpecified = true
            };
            EmailAddress emailAddr = new EmailAddress
            {
                Address = "Kaley_McMohan@example.com"
            };
            
            PhysicalAddress address = new PhysicalAddress
            {
                Line1 = "123 Mary Ave",
                City = "Sunnyvale",
                CountrySubDivisionCode = "CA",
                CountryCode = "USA",
                PostalCode = "94086"
            };

            customer.PrimaryEmailAddr = emailAddr;
            customer.BillAddr = address;
            customer.ShipAddr = address;
            
            DataService service = new DataService(context);
            Customer addedCustomer = service.Add<Customer>(customer);
            return addedCustomer;
        }

        public static CompanyInfo GetCompanyInfo(ServiceContext context)
        {
            QueryService<CompanyInfo> entityQuery = new QueryService<CompanyInfo>(context);
            List<CompanyInfo> companyInfo = entityQuery.ExecuteIdsQuery("SELECT * FROM CompanyInfo").ToList<CompanyInfo>();
            return companyInfo[0];  
        }
    }
}