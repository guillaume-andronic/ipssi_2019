#!/usr/bin/python2.6
# coding: utf-8

import os
import datetime
import sys
from datetime import timedelta

def sla(tps):
    calcul =((365.25*24*3600*1 - 365.25*24*3600*tps/100))
    print()
    affichage = datetime.timedelta( 0, calcul)
    return affichage

if __name__ == '__main__':
    print(sla(float(sys.argv[1])))
