from encryptedgiftsale import EncryptedGiftSale
import json

class Test_EncryptedGiftSale:
    def test_successful_encryptedgiftsale(self):
        try:
            myEncryptedGiftSale = EncryptedGiftSale(122,1.00,"C8C8F9536826D5450E734953206E7F4DC6812C6858037F5ABF23D9F83F948AF7","9012090B06349B000056")
            response = myEncryptedGiftSale.process()
            print response
            data = response.json()
            print data["TextResponse"]
            print("-------------------------------")
            print("Testing: AcctNo == '605011XXXXXXXXX0146'")
            print("-------------------------------")
            assert data["AcctNo"] == "605011XXXXXXXXX0146"
        except AssertionError as err:
            print("AcctNo was not equal to the value '605011XXXXXXXXX0146'")
            print("Adding additional text")
            print(err)
            raise