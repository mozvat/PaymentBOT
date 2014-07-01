clear
while true
	do
		echo "Git Status: :" 
		git status 
		echo "----------------------------------------------"
		echo "Pushing latest RaspberryPI Version from GitHub" 
		echo "GitHub/mozvat/RaspberryPI"
		sleep 1		
		echo "."
		sleep 1
		echo "."
		sleep 1
		git push
		echo "---------------------------"
		sleep 1000
	done
