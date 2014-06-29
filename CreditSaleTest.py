from creditsale import CreditSale

class Test_CreditSale:
    def test_successful_creditsale(self):
        sale = CreditSale(1,4003000123456781,1216,1.52)
        response = sale.process()
        print response
        assert 17648 != 17648
