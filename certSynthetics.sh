say "Beetle Juice now awake"

while true
    do
        echo "----------------------------------------------"
		echo "Pulling latest RaspberryPI Version from GitHub" 
		echo "Accessing GitHub/mozvat/RaspberryPI"
		sleep 1		
		echo "."
		sleep 1
		echo "."
		sleep 1
		echo "---------------------------"
		echo "Executing: Gift-Transaction"
		echo "Test file: test_giftsale.py"		
		sleep 1
		echo "Processing..."		
		nosetests test_giftsale.py
		echo "---------------------------"
		echo "Executing: Credit-Transaction"
 		echo "Test file: test_creditsale.py"
 		sleep 1
		echo "Processing..."
		nosetests test_creditsale.py
		echo "---------------------------"
		echo "Executing: Encrypted Credit-Transaction"
		echo "Test file: test_encryptedcreditsale.py"
		sleep 1
		echo "Processing..."
		nosetests test_encryptedcreditsale.py
                echo "---------------------------"
		echo "Executing: Encryped Gift-Transaction"
		echo "Test file: test_encryptedgiftsale.py"
		sleep 1
		echo "Processing..."
		nosetests test_encryptedgiftsale.py
		sleep 1
		echo "."
		sleep 1
		echo "."
		sleep 1
		echo "Hibernating for 10 minutes..."
		sleep 600
  	done
