print "Sending a Prepaid transaction to Mercury's certifiation network..."

import json
import requests
from requests.auth import HTTPBasicAuth

print "URL: https://w1.mercurycert.net/PaymentsAPI/Prepaid/Sale"

url = 'https://w1.mercurycert.net/PaymentsAPI/Prepaid/Sale'


payload = {'InvoiceNo': '3',
           'RefNo': '3',
           'Memo': 'Ozvat Python test',
           'EncryptedFormat': 'MagneSafe',
           'AccountSource': 'Swiped',
           'EncryptedBlock': 'C8C8F9536826D5450E734953206E7F4DC6812C6858037F5ABF23D9F83F948AF7',
           'EncryptedKey': '9012090B06349B000056',           
           'Purchase': '1.00'
           }
print payload
r = requests.post(url, data=json.dumps(payload), auth=('118725340908147', 'xyz'))

print r.text

