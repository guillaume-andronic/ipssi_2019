#!/bin/bash

# affiche la sortie standard vers un fichier /tmp/ls.log
ls -l > /tmp/ls.log
	echo "ls ok"

#affiche la sortie d'erreur vers un fichier /tmp/ls_err.log
ls -l /etc/passwd || echo "ls erreur " >> /tmp/ls_err.log

#affiche si le ls a fonctionné (c'est à dire l'exit code)
ls -l
if [ "$?" -ne "0" ]; then
  echo "ls FAIL"
exit
fi
