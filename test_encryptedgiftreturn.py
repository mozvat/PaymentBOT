'''
    Author: mozvat
    
    The EncryptedGiftSale class is responsible for accepting the minimum required arguments to request
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

class EncryptedGiftReturn(object):
    def __init__(self, InvoiceNo, Amount, EncryptedBlock, EncryptedKey):
        self.invoiceNo = InvoiceNo
        self.purchase = Amount
        self.encryptedBlock = EncryptedBlock
        self.encryptedKey = EncryptedKey
    
    def process(self):
        # TranType: {Credit,PrePaid, PayPal, etc} / TranCode {Sale, Return, Void}'
        url = 'https://w1.mercurycert.net/PaymentsAPI/Prepaid/Sale'
        
        payload = {
                    "InvoiceNo": self.invoiceNo,
                    "RefNo": self.invoiceNo,
                    'Memo': 'Ozvat-V3 PaymentBOT',
                    "Purchase": self.purchase,
                    "Frequency": "OneTime",
                    "RecordNo": "RecordNumberRequested",
                    "EncryptedFormat": "MagneSafe",
                    "AccountSource": "Swiped",
                    "EncryptedBlock": self.encryptedBlock,
                    "EncryptedKey": self.encryptedKey,
                    "TerminalName": "MPS Terminal",
                    "ShiftID": "MPS Shift",
                    "OperatorID": "MPS Operator"
                    }
        
        response = API.post(url, data=json.dumps(payload), auth=('112438931977591', 'xyz'))
        return response

'''
    ------------------------
    ---Unit test script ----
    ------------------------
    
    
    Use below code for quick check testing,
    otherwise leverage "nosetests"


sale = EncryptedGiftSale(12345,1.00,"C8C8F9536826D5450E734953206E7F4DC6812C6858037F5ABF23D9F83F948AF7","9012090B06349B000056")
response = sale.process()



data = response.json()
print "Invoice Number: " + data['InvoiceNo']
print "Account Number: " + data['AcctNo']
print "Transaction Status: " + data['CmdStatus']
print "Transaction Response: " + data['TextResponse']
print sale

'''
