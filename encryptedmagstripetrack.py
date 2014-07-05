'''
    Author: mozvat
    
    The ParseResponse class is responsible for accepting a track data argument and parsing the response into a json data variable.
    
    #Specificity guidelines:
    
    This class:
    - will NOT format response data from Web Services. It will allow the consumer to format the
    response.
    - However, this class WILL format input data and transform to the approrpriate request format.
'''

import json
import sys

class EncryptedMagStripeTrack(object):

    encryptedBlock = None
    encryptedKey = None
    
    def __init__(self, trackData):
        self.trackData = trackData
        containsEncryptedBlock, containsEncryptedKey, genericData = trackData.split("||")
        #print "Contains EncrypedBlock: " + containsEncryptedBlock
        #print "Contains EncrypedKey: " + containsEncryptedKey
        generic1, generic2, generic3, encryptedBlock = containsEncryptedBlock.split("|")
        self.encryptedBlock = encryptedBlock
        generic4, generic5, generic6, generic7, encryptedKey, generic8 = containsEncryptedKey.split("|")
        self.encryptedKey = encryptedKey
        print self.encryptedBlock
        print self.encryptedKey

    def EncryptedBlock(self):
        return self.encryptedBlock

    def EncryptedKey(self):
         return self.encryptedKey



'''
    ------------------------
    ---Unit test script ----
    ------------------------
    
    
    Use this for quick check testing,
    otherwise leverage "nosetests"

file = open("swipe.txt", "r")
trackData = file.read()
#print "Track: " + trackData
data = EncryptedMagStripeTrack(trackData)
print "EB: " + data.encryptedBlock
print "EK: " + data.encryptedKey

#print "Encrypted Block: " + data.x


    ParseEncryptedTrack()
    response = myCreditSale.process()
    data = response.json()
    
    print data['CmdStatus']
    
    print data
    
'''

