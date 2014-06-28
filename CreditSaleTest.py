import unittest
from creditsale import CreditSale

class CreditSaleTest(unittest.TestCase):
    def test_one_approved_transaction(self):
        sale = CreditSale(1,4003000123456781,1216,1.52)
        sale.process()
        print sale.getResponse()
       # assert sale.response() == 17648.0
#python -m unittest
