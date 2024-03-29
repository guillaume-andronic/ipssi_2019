#!/usr/bin/python2.6
# coding: utf-8

import sys
import time
from math import floor

def sla(disponibilite):
    indisponibilite=3600*24*365.25*(1-(disponibilite/100))
    heure = int(indisponibilite // 3600)
    minute = indisponibilite % 3600 // 60
    seconde = indisponibilite % 3600 % 60 // 1

    return ("{}h {}m {}s".format(heure, floor(minute),seconde))


if __name__ == "__main__":
    print(sla(float(sys.argv[1])))