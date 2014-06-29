from creditsale import CreditSale
import json

class Test_CreditSale:
    def test_successful_creditsale(self):
        try:
            sale = CreditSale(1,4003000123456781,1216,1.52)
            response = sale.process()
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
