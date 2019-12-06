#!/bin/bash
dateday=$(date +%F:%R:%S)

site="www.google.com"
if curl -s -I $site >/dev/null ;then
	echo "$dateday internet ok" >> internet.log
else
	echo "$dateday internet FAIL" >> internet.log
fi

exit 0
