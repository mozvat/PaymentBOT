while true
	clear
	do
		echo "----------------------------------------------"
		echo "Pulling latest RaspberryPI Version from GitHub" 
		echo "Accessing GitHub/mozvat/RaspberryPI"
		sleep 1		
		echo "."
		sleep 1
		echo "."
		sleep 1
		git pull
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
	done
