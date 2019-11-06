if curl -s -I $1 >/dev/null ;then
		echo "OK"
	else
		echo "FAIL"
		exit 2
	fi
