'''
Author: mozvat

The CreditSale class is responsible for accepting the minimum required arguments to request
a payment authorization via a HTTP POST request to Mercury's
web services.  It will return the raw response in JSON format.

#Specificity guidelines:

This class:
- will NOT format response data from Web Services. It will allow the consumer to format the
response.
- However, this class WILL format input data and transform to the approrpriate request format.
- will NOT expose any public attributes. This class is designed with a command pattern in mind and
not deisned to hold stateful data. 
'''

import json
import lib.requests.api as API   
from lib.requests.auth import HTTPBasicAuth

class CreditSale(object):
    def __init__(self, InvoiceNo, AcctNo, ExpDate, Amount):
        self.invoiceNo = InvoiceNo
        self.acctNo = AcctNo
        self.expDate = ExpDate
        self.purchase = Amount

    def process(self):        
        # TranType: {Credit,PrePaid, PayPal, etc} / TranCode {Sale, Return, Void}'
        url = 'https://w1.mercurycert.net/PaymentsAPI/Credit/Sale'

        payload = {'InvoiceNo': self.invoiceNo,
                    'RefNo': self.invoiceNo,
                    'Memo': 'Ozvat-v2',
                    'AcctNo': self.acctNo,
                    'ExpDate': self.expDate,
                    'Purchase': self.purchase
                    }

        response = API.post(url, data = json.dumps(payload), auth=('112438931977591', 'xyz'))   
        return response

'''
------------------------
---Unit test script ----
------------------------


Use this for quick check testing,
otherwise leverage "nosetests"

'''


'''
myCreditSale = CreditSale(1,4003000123456781,1216,1.52)
response = myCreditSale.process()
data = response.json()

print data['CmdStatus']

#print data
'''


