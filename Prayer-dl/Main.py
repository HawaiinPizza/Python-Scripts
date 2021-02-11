#!/bin/python
# Prayer day

# For using configuration/global variables
from Config import * 

# For stroing the dates and times fo the prayers
import datetime

import DL
import sys

if City == "":
    print("City variable is not set/is incorrect. refer to https://prayertimes.date/api/docs/cities")
    sys.exit(2)

PRAYER_MAP=DL.load()


def getDay(year, month, day):
    date = datetime.datetime(year, month, day)
    today = datetime.datetime.today()
    temp = datetime.datetime(today.year, today.month, today.day)

    if( date>= temp ):
        try:
            return PRAYER_MAP[datetime.datetime(year, month, day)]
        except KeyError:
            print("Going to download prayers")
            DL.save()
            return PRAYER_MAP[datetime.datetime(year, month, day)]
    else:
        sys.stderr.write("Date in past, cannot do that. If demand I'll add it")
        sys.exit(2)

def nextPrayer():
    now = datetime.datetime.today()
    today = getDay(now.year, now.month, now.day)
    for prayer in prayers:
        if( today[prayer] > now):
            return (prayer, today[prayer].strftime("%H:%M") )
    return None



x= nextPrayer()
if (x!=None):
    print(x[0], x[1])
# data=getDay(2020, 12, 29)
# print("FAJR", data['Fajr'])
