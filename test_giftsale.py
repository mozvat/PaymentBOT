from giftsale import GiftSale
import json

class Test_GiftSale:
    def test_successful_giftsale(self):
        try:
            sale = GiftSale(123,7712950000000000316,1216,1.57)
            response = sale.process()
            data = response.json()
            print("-------------------------------")
            print("Testing: AcctNo == 771295XXXXXXXXX0316")
            print("-------------------------------")
            assert data["AcctNo"] == "771295XXXXXXXXX0316"
	   # print data
        except AssertionError as err:
            print("RESULTS: AcctNo was not equal to the value 771295XXXXXXXXX0316")
            print(err)
            raise
