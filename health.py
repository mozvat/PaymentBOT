#!/usr/bin/env python


import os
'''
from processorstatus import ProcessorStatus
'''
import sys

# print header
print "Content-type: text/html\n\n"
print "<h1>PaymentsBOT running on Orion:RaspberryPI</h1>"
client_ip=os.environ["REMOTE_ADDR"]

print "<h2>POS http client requesting the health of PaymentBOT</h2>"
print "Your client IP is recorded for transaction history: " + client_ip + "<br>"
'''
processorStatus  = ProcessorStatus()
response = processorStatus.get()

print "<h2>PaymentsBOT response payload</h2>"
print response

data = response.json()

print "Total Credit Transactions: " + data["TotalCreditSales"]
print "<br>Failed Credit Transactions: " + data["FailedCreditSales"]
print "<br>Total Gift Sales: " + data["TotalGiftSales"]
print "<br>Failed Gift Sales: " + data["FailedGiftSales"]
print "<h3>-------------Transaction raw reponse-------------</h3>"
print data
'''
