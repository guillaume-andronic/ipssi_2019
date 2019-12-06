#!/bin/bash
#If block

if ls $1 >/dev/null 2>/dev/null ;then
    echo "ls ok"
    ls $1 >> /tmp/ls.log
else
    echo "ls FAIL"
    ls $1 2>> /tmp/ls_err.log
    exit 2
fi
exit 0
