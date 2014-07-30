#!/usr/bin/env python

import os
import sys
from processorstatus import ProcessorStatus

# print header
print "Content-type: text/html\n\n"
print "<h1>PaymentsBOT running on Orion:RaspberryPI</h1>"
client_ip=os.environ["REMOTE_ADDR"]

print "<h2>POS http client requesting the health of PaymentBOT</h2>"
print "Requesting client IP: " + client_ip + "<br>"

processorStatus  = ProcessorStatus()
response = processorStatus.get()

print "<h2>PaymentsBOT response payload</h2>"
print "<h3>--------------Transaction history----------------</h3>"
print "Total Credit Transactions:" + response["TotalCreditSales"]
print "<br>Failed Credit Transactions: " + response["FailedCreditSales"]
print "<br>Total Gift Sales: " + response["TotalGiftSales"]
print "<br>Failed Gift Sales: " + response["FailedGiftSales"]
print "<h3>-------------Transaction raw reponse-------------</h3>"
print response
