say "I am Beetle Juice"

while true
    do
        echo "----------------------------------------------"
		echo "@BG: I am running synthetics."
		sleep 1		
		echo "."
		sleep 1
		echo "."
		sleep 1
		echo "@BG: Executing a Gift transaction."
		echo "Test file: test_giftsale.py"		
		sleep 1
		echo "Processing..."		
		nosetests test_giftsale.py
		echo "---------------------------"
		sleep 1
		echo '.'
		sleep 1
		echo '.'
		sleep 1
		echo "@BG: Executing a Credit transaction."
 		echo "Test file: test_creditsale.py"
 		sleep 1
		echo "Processing..."
		nosetests test_creditsale.py
		echo "---------------------------"
		sleep 1
		echo '.'
		sleep 1
		echo '.'
		sleep 1
		echo "@BG: Executing an encrypted Credit transaction."
		echo "Test file: test_encryptedcreditsale.py"
		sleep 1
		echo "Processing..."
		nosetests test_encryptedcreditsale.py
                echo "------------------------------"
		sleep 1
		echo '.'
		sleep 1
		echo '.'
		sleep 1
		echo "@BG: Executing an encryped Gift transaction."
		echo "Test file: test_encryptedgiftsale.py"
		sleep 1
		echo "Processing..."
		nosetests test_encryptedgiftsale.py
		echo "------------------------------"
		sleep 1
		echo "."
		sleep 1
		echo "."
		sleep 1
		echo "@BG: I am hibernating for 20 minutes..."
		sleep 1200
  	done
