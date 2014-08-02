while true
    do
        echo "----------------------------------------------"
		echo "@PB: I am pushing to production."
		sleep 1		
		echo "."
		sleep 1
		echo "."
		sleep 1
		echo "Copying Index.html for PaymentBOT website..."		
                echo "---------------------------"
		cp index.html /var/www
		sleep 1
		echo '.'
		sleep 1
		echo '.'
		sleep 1
		echo "@PB: Copying sale.py script for PaymentBOT webservice."
		echo "---------------------------"
		cp sale.py /usr/lib/cgi-bin		
		sleep 1
		echo '.'
        sleep 1
        echo '.'
        sleep 1
        echo "@PB: Copying health.py script for PaymentBOT webservice ..."
		echo "---------------------------"
		cp health.py /usr/lib/cgi-bin
		sleep 1
		echo '.'
		sleep 1
		echo '.'
		sleep 1
		echo "@PB: I am hibernating for 20 minutes..."
		sleep 1200
  	done
