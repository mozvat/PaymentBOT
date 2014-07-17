clear
say "I am Rigel"
while true
	do
		clear
		echo "@Rigel: I am invoking the git status command"
		sleep 3
		echo 
		echo "---------------Git Status Results--------------------"
		git status
		echo
		sleep 3
		echo "@Rigel: I am invoking the git push command"
		sleep 3
		echo
		echo "---------------Git Push Results--------------------"
		git push
		echo	
		sleep 3
		echo '.'
		sleep 1
		echo '.'
		sleep 1
		echo "@Rigel: I am hibernating for 5 minutes..."
		sleep 300
	done
say "Rigel is sleeping"
