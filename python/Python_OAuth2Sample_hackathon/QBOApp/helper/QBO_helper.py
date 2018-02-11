"""
    Helper module to create supporting entities for Bill in QBO
"""
import json
import uuid
import datetime
import requests
from enum import Enum
import sys

def create_item(config):
    """
        POST request to create an Inventory Item in QBO
        Refer here for other Inventory fields: https://developer.intuit.com/docs/api/accounting/item
    """
    date = datetime.date.today()

    try: 
        account_hs, income_account = create_account(config, AccountType.INCOME)
        account_hs, expense_account = create_account(config, AccountType.EXPENSE)
        account_hs, asset_account = create_account(config, AccountType.ASSET)

        if account_hs == 401:
            return account_hs, {}
        # for both 400 error message and 200 successful, print to screen
    except:
        print("Unexpected error:", sys.exc_info()[0])

    url = config['qbo_base_url'] + '/v3/company/' + config['realm_id'] + '/item?minorversion=12'

    item =  {
                "Name": "Item_demo_" + str(uuid.uuid4()),
                "UnitPrice": 100,
                "Type": "Inventory",
                "IncomeAccountRef": {
                    "name": income_account["Name"],
                    "value": income_account["Id"]
                },
                "ExpenseAccountRef": {
                    "name": expense_account["Name"],
                    "value": expense_account["Id"]
                },
                "AssetAccountRef": {
                    "name": asset_account["Name"],
                    "value": asset_account["Id"]
                },
                "InvStartDate": date.isoformat(),
                "TrackQtyOnHand": True,
                "QtyOnHand": 50
            }
    
    headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": "Bearer " + config['access_token']
            }
    
    r = requests.post(url, headers=headers, data=json.dumps(item))
    print(r.status_code)
    print (r.content)

    try:
        response = r.json()["Item"]
    except:
        response = r.content
    return r.status_code, response
    
def create_vendor(config):
    """
        POST request to create a Vendor in QBO
        Refer here for other Vendor fields: https://developer.intuit.com/docs/api/accounting/vendor
    """
    url = config['qbo_base_url'] + '/v3/company/' + config['realm_id'] + '/vendor?minorversion=12'

    vendor = {
                "DisplayName": "Vendor_demo_" + str(uuid.uuid4()),
                "CompanyName": "ABC Designing Firm",
                "PrimaryPhone": {
                    "FreeFormNumber": "123-445-6789"
                },
                "PrimaryEmailAddr": {
                    "Address": "info@abcdesigning.net"
                },
                "BillAddr": {
                    "Line1": "123 Mary Ave",
                    "City": "Sunnyvale",
                    "CountrySubDivisionCode": "CA",
                    "Country": "USA",
                    "PostalCode": "1111" 
                }
            }

    headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": "Bearer " + config['access_token']
            }

    r = requests.post(url, headers=headers, data=json.dumps(vendor))
    print (r.status_code)
    print (r.content)

    try:
        response = r.json()["Vendor"]
    except:
        response = r.content
    return r.status_code, response

def create_account(config, account_type):
    """
        POST request to create an Account depending on Account type in QBO
        Refer here for other Account fields: https://developer.intuit.com/docs/api/accounting/account
    """
    url = config['qbo_base_url'] + '/v3/company/' + config['realm_id'] + '/account?minorversion=12'

    if account_type.name == AccountType.ASSET.name:
        account_sub_type = "Inventory"
    elif account_type.name == AccountType.INCOME.name:
        account_sub_type = "SalesOfProductIncome"
    else:
        account_sub_type = "SuppliesMaterialsCogs"

    account = { 
                "Name": "Account_demo_" + str(uuid.uuid4()),
                "Description": "Account of type: " + account_type.value,
                "AccountType": account_type.value,
                "AccountSubType": account_sub_type
            }
    
    headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": "Bearer " + config['access_token']
            }

    r = requests.post(url, headers=headers, data=json.dumps(account))
    print (r.status_code)
    print (r.content)
    
    try:
        response = r.json()["Account"]
    except:
        response = r.content

    return r.status_code, response

class AccountType(Enum):
    """
        Enum for different Account types used in this sample. For other types of Account, go to https://developer.intuit.com/docs/api/accounting/account
    """
    ASSET = "Other Current Asset"
    INCOME = "Income"
    EXPENSE = "Cost of Goods Sold"