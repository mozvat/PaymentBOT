from giftsale import GiftSale
from creditsale import CreditSale
import sys

print "---------------------------------"    
print "Welcome to the Python POS system!"
print "---------------------------------\n\n"
print "---------------------------------"
print "-            MENU              -"
print "---------------------------------"
print "[1] - Credit Sale"
print "[2] - Gift Sale"
print "---------------------------------"

selection = input("Select Transaction type: ")

if selection == 1:
    myCreditSale = CreditSale(12)
    myCreditSale.process()
else:
    myGiftSale = GiftSale(12)
    myGiftSale.process()

def main(argv=None):
    if argv is None:
        argv = sys.argv
    print "Script Name: " + sys.argv[0]
