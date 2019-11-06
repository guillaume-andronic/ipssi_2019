#!/bin/bash

set -e

if [ -f efface_moi ]; then
	rm efface_moi
else
	echo "nothing to do"
fi
