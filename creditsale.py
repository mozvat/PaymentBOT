print "Sending a Credit transaction to Mercury's certification network..."

import json   
import requests   
from requests.auth import HTTPBasicAuth

class CreditSale(object):
    def __init__(self, InvoiceNo):
        self.invoiceNo = InvoiceNo

    def process(self):        
        # TranType: {Credit,PrePaid, PayPal, etc} / TranCode {Sale, Return, Void}'
        url = 'https://w1.mercurycert.net/PaymentsAPI/Credit/Sale'

        payload = {'InvoiceNo': '514',
                    'RefNo': '5141',
                    'AcctNo': '4003000123456781',
                    'ExpDate': '1215',
                    'Purchase': '1.00'}

        print payload

        r = requests.post(url, data = json.dumps(payload), auth=('112438931977591', 'xyz'))       
    
        print r.text

