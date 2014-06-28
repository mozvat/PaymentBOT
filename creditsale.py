import json   
import lib.requests.api as API   
from lib.requests.auth import HTTPBasicAuth

class CreditSale(object):
    def __init__(self, InvoiceNo, AcctNo, ExpDate, Amount):
        self.invoiceNo = InvoiceNo
        self.acctNo = AcctNo
        self.expDate = ExpDate
        self.purchase = Amount
        self.response = ""
        print "Initializing the CreditSale payload..."

    def process(self):        
        # TranType: {Credit,PrePaid, PayPal, etc} / TranCode {Sale, Return, Void}'
        url = 'https://w1.mercurycert.net/PaymentsAPI/Credit/Sale'

        payload = {'InvoiceNo': self.invoiceNo,
                    'RefNo': self.invoiceNo,
                    'Memo': "Ozvat",
                    'AcctNo': self.acctNo,
                    'ExpDate': self.expDate,
                    'Purchase': self.purchase}

        print payload

        r = API.post(url, data = json.dumps(payload), auth=('112438931977591', 'xyz'))       
 
        self.response = r.text
        #print self.response

    def getResponse(self):
        return self.response

    def setResponse(self, value):
        self.response = value

#unit test script
#myCreditSale = CreditSale(1,4003000123456781,1216,1.52)
#myCreditSale.process()
#print myCreditSale.getResponse()
