print "Sending a Prepaid transaction to Mercury's certification network..."

import json
import lib.requests.api as API
from lib.requests.auth import HTTPBasicAuth

class GiftSale(object):
    def __init__(self, InvoiceNo):
        self.invoiceNo = InvoiceNo

    def process(self):
        # TranType: {Credit,PrePaid, PayPal, etc} / TranCode {Sale, Return, Void}'
        url = 'https://w1.mercurycert.net/PaymentsAPI/Prepaid/Sale'

        payload = {"InvoiceNo":"291",
                    "RefNo":"214",
                    "AcctNo":"7712950000000000316",
                    "ExpDate":"1215",
                    "Purchase":"1.00"}
            
        r = API.post(url, data=json.dumps(payload), auth=('112438931977591', 'xyz'))
    
        print r.text



myGiftSale = GiftSale(12)
myGiftSale.process()
