from encryptedcreditsale import EncryptedCreditSale
import json

class Test_EncryptedCreditSale:
    def test_successful_creditsale(self):
        try:
            myEncryptedCreditSale = EncryptedCreditSale(12,'2F8248964608156B2B1745287B44CA90A349905F905514ABE3979D7957F13804705684B1C9D5641C','9500030000040C200026',1.52)
            response = myEncryptedCreditSale.process()
            data = response.json()
            print("-------------------------------")
            print("Testing: CmdStatus == 'Approved'")
            print("-------------------------------")
            print("CmdStatus results: " + data['CmdStatus'])
            assert data['CmdStatus'] == "Approved"
        except AssertionError as err:
            print("CmdStatus was not equal to the value 'Approved'")
            print(err)
            raise
