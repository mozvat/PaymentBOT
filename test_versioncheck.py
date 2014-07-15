from netepay import NETePay
import json

class Test_NETePayVersion:
    def test_cert_netepayversion(self):
        try:
            netepay = NETePay()
            version = netepay.version()
            data = response.json()
            print("-------------------------------")
            print("Testing: Cert Version == 1234")
            print("-------------------------------")
            assert data["AcctNo"] == "771295XXXXXXXXX0316"
        # print data
        except AssertionError as err:
            print("RESULTS: AcctNo was not equal to the value 771295XXXXXXXXX0316")
            print(err)
        raise


StringBuilder builder = new StringBuilder();
builder.Append("<?xml version=\"" + "1.0\"?>");
builder.Append("<TStream>");
builder.Append("<Admin>");
builder.Append("<MerchantID>" + ProcessingEnvironment.Instance.MerchantID + "</MerchantID>");
builder.Append("<TranCode>ServerVersion</TranCode>");
builder.Append("<Memo>Ozvat ServerVersion Test</Memo>");
builder.Append("</Admin>");
            builder.Append("</TStream>");