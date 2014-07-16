clear
say "I am Rigel"
while true
	do
		echo "@Rigel: I am invoking Git status"
		sleep 3
		echo 
		echo "---------------Git Status Results--------------------"
		git status
		echo
		sleep 3
		echo "@Rigel: I am invoking Git push"
		sleep 3
		echo
		echo "---------------Git Push Results--------------------"
		git push
		echo	
		sleep 3
		echo "______________________________________"
		echo "@Rigel: I am hibernating for 5 minutes"
		echo "______________________________________"
		sleep 300
	done
say "Rigel is sleeping"
