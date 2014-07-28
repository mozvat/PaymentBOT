#!/usr/bin/env python

import os
from processorstatus import ProcessorStatus
import sys

# print header
print "Content-type: text/html\n\n"
print "<h1>PaymentsBOT.Info running on Orion:RaspberryPI</h1>"
query_string=os.environ["QUERY_STRING"]

print "<h2>POS http client requesting a status of Payment Authorization Parent</h2>"
print "query_string: " + query_string + "<br>"

print "<h2>Transaction query_string sent to PaymentsBOT.Info</h2>"
arg_list=query_string.split('&')
#print arg_list

i=1
for arg in arg_list:
    key, value=arg.split('=')
    print "key "+str(i)+": "+key+"<br>"
    print"value "+str(i)+": "+value+"<br>"
    i +=1

#Wait for swipe
#trackData = "%B5499000090006781^TEST/MPS^15120000000000000?;5499000090006781=15120000000000000000?|0600|74F1C98C2EF08240B92D66C96F17EA217155BD168C6A394B0B318E834CDE6D07B5F00FC8C9C02ED4486E95681D169B2D|2B0FF19B93EAE51780787276264A029276A3BDCA2622A3FD12E3F6A5714B885984F2096B7E9FE1A6||61401000|D2CA4A6339A00C08E7A8DCDD80447BFFA46F24F3386AD7B46EDD44622B3E28FDCC376907B3555C67B826AF8A21C5851A1F5A7AD01DFAE799|B06349B042812AA|BDAAB3EA6505F532|9012090B06349B00006E|B973||1000"

#containsEncryptedBlock, containsEncryptedKey, genericData = trackData.split("||")
#print containsEncryptedKey
#generic1, generic2, generic3, encryptedBlock = containsEncryptedBlock.split("|")

#generic4, generic5, generic6, generic7, encryptedKey, generic8 = containsEncryptedKey.split("|")

#myEncryptedCreditSale = EncryptedCreditSale(122, encryptedBlock, encryptedKey, 1.25)
processStatus = ProcessorStatus();
response = processorStatus.process()

print "<h2>PaymentsBOT.info Processor Status</h2>"
print response + "<br><br>"

data = response.json()

print "<h3>----------PaymentBOT Server Status -----------------------</h3>"
print "Total Credit Sales: " + data["TotalCreditSales"]
print "<br>Failed Credit Sales: "  + data["FailedCreditSales"]
print "<br>Total Gift Sales: " + data["TotalGiftSales"]
print "<br>Failed Gift Sales: " + data["FailedGiftSales"]
print "<br>Total Encrypted Credit Sales: " + data["TotalEncryptedCreditSales"]
print "<br>Failed Encrypted Credit Sales: " + data["FailedEncryptedCreditSales"]
print "<br>Total Encrypted Gift Sales: " + data["TotalEncryptedGiftSales"]
print "<br>Failed Encrypted Gift Sales: " + data["FailedEncryptedGiftSales"]
print "<h3>------------------------------------------------------------</h3>"
print data

