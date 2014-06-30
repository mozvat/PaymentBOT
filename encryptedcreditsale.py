
import json
import lib.requests.api as API
from lib.requests.auth import HTTPBasicAuth

class EncryptedCreditSale(object):
    def __init__(self, InvoiceNo, EncryptedBlock, EncryptedKey, Amount):
        self.invoiceNo = InvoiceNo
        self.encryptedBlock = EncryptedBlock
        self.encryptedKey = EncryptedKey
        self.purchase = Amount
    
    def process(self):
        # TranType: {Credit,PrePaid, PayPal, etc} / TranCode {Sale, Return, Void}'
        url = 'https://w1.mercurycert.net/PaymentsAPI/Credit/Sale'
        
        payload = {'InvoiceNo': self.invoiceNo,
            'RefNo': self.invoiceNo,
            'Memo': 'Ozvat',
            'AcctNo': self.acctNo,
            'ExpDate': self.expDate,
            'Purchase': self.purchase}
        
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




print "Let's collide the Protons together and make a nuclear experience"

import json
import requests
from requests.auth import HTTPBasicAuth

url = 'https://w1.mercurycert.net/PaymentsAPI/Credit/Sale'

payload = {'InvoiceNo': '12',
           'Memo': 'Ozvat Python test',
           'Purchase': '1.00',
           'Frequency': 'OneTime',
           'RecordNo': 'RecordNumberRequested',
           'EncryptedFormat': 'MagneSafe',
           'AccountSource': 'Swiped',
           'EncryptedBlock': '2F8248964608156B2B1745287B44CA90A349905F905514ABE3979D7957F13804705684B1C9D5641C',    
           'EncryptedKey': '9500030000040C200026'
           }

r = requests.post(url, data = json.dumps(payload), auth=('118725340908147', 'xyz'))

print r.text



