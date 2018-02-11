"""
    Main module that creates and gets Bill in QBO
"""
import sys
import datetime
import json
import requests
from .helper import QBO_helper

def create_bill(config):
    """ 
        POST request to create a Bill in QBO
        Refer here for other available Bill fields and other QBO entities: https://developer.intuit.com/docs/api/accounting/bill
    """

    print("**** Create bill ****")

    date = datetime.date.today()
    due_date = date + datetime.timedelta(days=30)

    try: 
        item_hs, item = QBO_helper.create_item(config)
        vendor_hs, vendor = QBO_helper.create_vendor(config)
        
        if item_hs == 401 or vendor_hs == 401:
            return 401, {}
    except:
        print("Unexpected error:", sys.exc_info()[0])

    url = config['qbo_base_url'] + '/v3/company/' + config['realm_id'] + '/bill?minorversion=12'

    try: 
        bill = {
                    "TxnDate": date.isoformat(),
                    "PrivateNote": "This is my first time creating a bill in QBO.",
                    "Line": [{
                        "Amount": 200,
                        "DetailType": "ItemBasedExpenseLineDetail",
                        "ItemBasedExpenseLineDetail": {
                            "BillableStatus": "NotBillable",
                            "ItemRef": {
                                "name": item["Name"],
                                "value": item["Id"]
                            },
                            "UnitPrice": 100,
                            "Qty": 2,
                            "TaxCodeRef": {
                                "value": "NON"
                            }
                        }
                    }],
                    "VendorRef": {
                        "name": vendor["DisplayName"],
                        "value": vendor["Id"]
                    },
                    "DueDate": due_date.isoformat(),
                    "Balance": 200.0
                }

        headers = {
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + config['access_token']
                }

        r = requests.post(url, headers=headers, data=json.dumps(bill))
        print (r.content)
        return r.status_code, r.json()
    except: 
        print("Unexpected error:", sys.exc_info()[0])


def get_bill(config, bill_id):
    """
        GET request to retrieve a Bill in QBO
        Refer here for other available Bill fields and other QBO entities: https://developer.intuit.com/docs/api/accounting/bill
    """
    print("****  Read bill  ****")

    url = ''
    url += config['qbo_base_url'] + '/v3/company/' + config['realm_id'] + '/bill/' + bill_id + '?minorversion=12'

    headers = {
                "Accept": "application/json",
                "Authorization": "Bearer " + config['access_token']
            }

    try: 
        r = requests.get(url, headers=headers)
        print (r.content)
        return  r.status_code, r.json()
    except:
        print ("Unexpected error:", sys.exc_info()[0])
    
