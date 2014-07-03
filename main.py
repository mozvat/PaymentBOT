from giftsale import GiftSale
from creditsale import CreditSale
import sys

print "--------------------------------------"
print "Welcome to the RaspberryPI POS system!"
print "--------------------------------------\n\n"
print "---------------------------------"
print "-            MENU              -"
print "---------------------------------"
print "[1] - Start listening"
print "[2] - Congifuration"
print "[3] - Status"
print "---------------------------------"

selection = input("Selection: ")

if selection == 1:
    #Wait for Swipe:
    trackData = raw_input("\n\nSwipe...\n\n")
    #    trackData = "%B5499000090006781^TEST/MPS^15120000000000000?;5499000090006781=15120000000000000000?|0600|74F1C98C2EF08240B92D66C96F17EA217155BD168C6A394B0B318E834CDE6D07B5F00FC8C9C02ED4486E95681D169B2D|---2B0FF19B93EAE51780787276264A029276A3BDCA2622A3FD12E3F6A5714B885984F2096B7E9FE1A6---||61401000|D2CA4A6339A00C08E7A8DCDD80447BFFA46F24F3386AD7B46EDD44622B3E28FDCC376907B3555C67B826AF8A21C5851A1F5A7AD01DFAE799|B06349B042812AA|BDAAB3EA6505F532|---9012090B06349B00006E---|B973||1000"

    containsEncryptedBlock,containsEncryptedKey,genericData = trackData.split("||")
    print containsEncryptedKey
    generic1, generic2, generic3, encryptedBlock = containsEncryptedBlock.split("|")

    generic4, generic5, generic6, generic7, encryptedKey, generic8 = containsEncryptedKey.split("|")

    print encryptedKey
    print encryptedBlock

    myEncryptedCreditSale = EncryptedCreditSale(122,1.00,encryptedBlock, encryptedKey)
    response = myEncryptedCreditSale.process()
    print response
    data = response.json()
    print data["TextResponse"]

#else:
#    print "Hello"
#myCreditSale = CreditSale(1234, AcctNo, ExpDate, 1.46)
#myCreditSale.process()



def main(argv=None):
    if argv is None:
        argv = sys.argv
    print "Arg Name: " + sys.argv[0]