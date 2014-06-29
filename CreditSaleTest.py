from creditsale import CreditSale
import json

class Test_CreditSale:
    def test_successful_creditsale(self):
        sale = CreditSale(1,4003000123456781,1216,1.52)
        response = sale.process()
        #print response
        data = response.json()
        assert data['CmdStatus'] == "Approved"

