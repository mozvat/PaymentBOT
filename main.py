from giftsale import GiftSale
from creditsale import CreditSale
from encryptedcreditsale import EncryptedCreditSale
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

    containsEncryptedBlock, containsEncryptedKey, genericData = trackData.split("||")
    print containsEncryptedKey
    generic1, generic2, generic3, encryptedBlock = containsEncryptedBlock.split("|")

    generic4, generic5, generic6, generic7, encryptedKey, generic8 = containsEncryptedKey.split("|")

    print encryptedKey
    print encryptedBlock

    myEncryptedCreditSale = EncryptedCreditSale(122,1.00 ,encryptedBlock, encryptedKey)
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