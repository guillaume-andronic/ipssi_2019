#!/usr/bin/python3

import sys
import calendar
from datetime import datetime
from tree import show_tree


def noel(allArg):
    if len(allArg) > 1:
        date_time_str = allArg[1]
        theDate = datetime.strptime(date_time_str, '%Y-%m-%d')
    else:
        theDate = datetime.now()


    c = calendar.TextCalendar(calendar.MONDAY)
    firstCalendar = c.formatmonth(theDate.year, theDate.month, 5, 1)
    firstCalendar = firstCalendar.replace(str(theDate.day), "("+str(theDate.day)+")", 1)
    
    c = calendar.TextCalendar(calendar.MONDAY)
    secondCalendar = c.formatmonth(theDate.year, 12, 5, 1)
    secondCalendar = secondCalendar.replace(" 25 ", "[25]", 1)


    if theDate.strftime('%Y-%m-%d') == str(theDate.year)+"-12-25":
        return show_tree(10)
    else:
        return firstCalendar+secondCalendar
if __name__ == "__main__":
    print(noel(sys.argv))