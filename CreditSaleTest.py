from creditsale import CreditSale

class TestExampleTwo:
    def test_c(self):
        sale = CreditSale(1,4003000123456781,1216,1.52)
        sale.process()
        print sale.getResponse()
        assert 17648 != 17648
