'''
Author: mozvat

The CreditReturn class is responsible for accepting the minimum required arguments to request
a payment authorization via a HTTP POST request to Mercury's
web services.  It will return the raw response in JSON format.
Adding to invoke CI.

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

class CreditReturn(object):
    def __init__(self, InvoiceNo, Token, Amount):
        self.invoiceNo = InvoiceNo
        self.refno = InoviceNo
        self.RecordNo = Token
        self.purchase = Amount

    def process(self):        
        # TranType: {Credit,PrePaid, PayPal, etc} / TranCode {Sale, Return, Void}'
        url = 'https://w1.mercurycert.net/PaymentsAPI/Credit/Return'

        payload = {'InvoiceNo': self.invoiceNo,
                    'RefNo': self.invoiceNo,
                    'Memo': 'Ozvat-v2',
                    'RecordNo': self.RecordNo,
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


myCreditReturn = CreditReturn(1,"cYiaGv9ZkPtXbq3uaLtxNoksqkz6DK+3KSBLJtuonxkiEgUQBCIQGqBR",1.52)
response = myCreditReturn.process()
data = response.json()

print data['CmdStatus']
print data['AcctNo'] #should equal 400555XXXXXX0480 if not, the encryption module is malfunctioning

print data

'''

