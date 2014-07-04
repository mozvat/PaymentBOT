from encryptedcreditsale import EncryptedCreditSale
import sys

print "--------------------------------------"
print "Welcome to the RaspberryPI POS system!"
print "--------------------------------------\n\n"



selection = 0

while (selection != 4):

    print "---------------------------------"
    print "-            MENU              -"
    print "---------------------------------"
    print "[1] - Start listening"
    print "[2] - Congifuration"
    print "[3] - Status"
    print "[4] - Quit"
    print "---------------------------------"

    selection = input("Selection: ")

    if selection == 1:

        merchantThreshold = 2
        transactionCount = 0

        while (merchantThreshold < transactionCount):
        
            #Wait for Swipe:
            trackData = raw_input("\n\nSwipe...\n\n")

            containsEncryptedBlock, containsEncryptedKey, genericData = trackData.split("||")
            print containsEncryptedKey
            generic1, generic2, generic3, encryptedBlock = containsEncryptedBlock.split("|")

            generic4, generic5, generic6, generic7, encryptedKey, generic8 = containsEncryptedKey.split("|")

            myEncryptedCreditSale = EncryptedCreditSale(122, encryptedBlock, encryptedKey, 1.25)
            response = myEncryptedCreditSale.process()
            print response
            data = response.json()
            print data["TextResponse"]
            transactionCount = transactionCount + 1
            print "Transaction count: " + transactionCount

    if  selection == 2:
        print "Congifigure"

    if  selection == 3:
        print "Status"

    else:
        print "Exiting System"



def main(argv=None):
    if argv is None:
        argv = sys.argv
    print "Arg Name: " + sys.argv[0]