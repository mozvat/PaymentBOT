'''
Author: mozvat

The ProcessorStatus class is responsible for reading and writing information regarding the 
test synthetic summary.

#Specificity guidelines:

This class:
- will NOT format response data from Web Services. It will allow the consumer to format the
response. (It will return JSON format.)
- However, this class WILL format input data and transform to the approrpriate request format.
- will NOT expose any public attributes. This class is designed with a command pattern in mind and
not deisned to hold stateful data. 
'''

import json
from json import dumps, load

class ProcessorStatus(object):
    def __init__(self):
        self.totalCreditSales = 0
	self.failedCreditSales = 0
	self.totalGiftSales = 0
	self.failedGiftSales = 0
	self.totalEncryptedCreditSales = 0
	self.failedEncryptedCreditSales = 0
	self.totalEncryptedGiftSales = 0
	self.failedEncryptedGiftSales = 0

    def Get(self):
	print("Get some data")        
	#with open("ProcessorStatus.json") as json_file:
    	#json_data = json.load(json_file)
    	#print(json_data)
    
    def Set(self):
        payload = {'InvoiceNo': self.invoiceNo,
                    'RefNo': self.invoiceNo,
                    'Memo': 'Ozvat-v2',
                    'AcctNo': self.acctNo,
                    'ExpDate': self.expDate,
                    'Purchase': self.purchase
                    }

    def Process(self):
	with open("processorlog.json", "w") as json_file:
		json.dump({
			'TotalCreditSales': self.totalCreditSales, 
			'FailedCreditSales': self.failedCreditSales,
			'TotalGiftSales': self.totalGiftSales
			}, json_file, sort_keys=True, indent=4, separators=(',', ': '))
	    	json_file.close()

	with open("processorlog.json") as json_file:
    		result = load(json_file)
		print result

'''
------------------------
---Unit test script ----
------------------------
Use this for quick check testing,
otherwise leverage "nosetests"
'''

processorStatus = ProcessorStatus()
processorStatus.Process() 
