from encryptedgiftsale import EncryptedGiftSale
import json

class Test_EncryptedGiftSale:
    def test_successful_encryptedgiftsale(self):
        try:
            myEncryptedGiftSale = EncryptedGiftSale(12,'2F8248964608156B2B1745287B44CA90A349905F905514ABE3979D7957F13804705684B1C9D5641C','9500030000040C200026',1.52)
            response = myEncryptedGiftSale.process()
            print response
            data = response.json()
            print data["TextResponse"]
            print("-------------------------------")
            print("Testing: AcctNo == '400555XXXXXX0480'")
            print("-------------------------------")
            #print("AcctNo results: " + data["AcctNo"])
            assert 1 == "NEED TO ASSERT DATA CORRECTLY BUT HAVE ENCRYPTION ISSUES"
#assert data["AcctNo"] == "400555XXXXXX0480"
        except AssertionError as err:
            print("AcctNo was not equal to the value '400555XXXXXX0480'")
            print(err)
            raise