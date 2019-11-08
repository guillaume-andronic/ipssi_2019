#!/bin/bash

cat /etc/passwd | cut -d: -f3 | tail -4

