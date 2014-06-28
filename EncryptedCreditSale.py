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


