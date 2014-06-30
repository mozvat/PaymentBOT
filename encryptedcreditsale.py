
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
                    'Memo': 'Ozvat Python test',
                    'Purchase': self.purchase,
                    'Frequency': 'OneTime',
                    'RecordNo': 'RecordNumberRequested',
                    'EncryptedFormat': 'MagneSafe',
                    'AccountSource': 'Swiped',
                    'EncryptedBlock': self.encryptedBlock,
                    'EncryptedKey': self.encryptedKey
                    }
    
        response = API.post(url, data = json.dumps(payload), auth=('118725340908147', 'xyz'))
        return response


'''
    ------------------------
    ---Unit test script ----
    ------------------------
    
    
    Use this for quick check testing,
    otherwise leverage "nosetests"
    
    '''


'''
    myCreditSale = CreditSale(1,2F8248964608156B2B1745287B44CA90A349905F905514ABE3979D7957F13804705684B1C9D5641C,9500030000040C200026,1.52)
    response = myCreditSale.process()
    data = response.json()
    
    print data['CmdStatus']
    
    #print data
'''