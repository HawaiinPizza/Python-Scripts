# Done because these are supposed to be global varaibles
from Config import *

import requests

import datetime
import sys

import pickle



def IntervalRequest( TimeSpan=TimeInterval):
        url="https://api.pray.zone/v2/times/"
        if  TimeSpan== Interval.DAILY:
                url=url+"today.json"
        elif  TimeSpan== Interval.WEEKLY:
                url=url+"this_week.json"
        elif  TimeSpan== Interval.MONTHLY:
                url=url+"this_month.json"
        
        try:
            print(url+City+"&school"+school)
            response=requests.get(url+City+"&school="+school)

            # This way, if 
            if response.status_code == 500:
                raise Exception
            else:
                return response
        

        except:
                sys.stderr.write("Internet is not connected/API keys are incorrect. Check Config.py")
                quit(1)

def convertDate(date):
        _date = datetime.datetime.fromisoformat(date)
                
        return _date

def convertTime(date, time):
        _time =  datetime.datetime.fromisoformat(date+" "+time)
        return _time
        
def Parse():
        # Parsing
        response=IntervalRequest().json()['results']['datetime'] 
        prayer_map={}
        for time in response:
            day={}    
            for prayer in prayers:
                    day[prayer] = convertTime(time['date']['gregorian'], time['times'][prayer])
            prayer_map[ convertDate(time['date']['gregorian']) ] = day
        return prayer_map
        

# Save and Parse were the same function
# But I decied to seperate them, to keep the API divdied
def save( File=File): 
    try:
        prayer_map = Parse() 
        with open(File, "wb+") as f:
                pickle.dump(prayer_map, f)
                return prayer_map
    except:
        print("City variable is not set/is incorrect. refer to https://prayertimes.date/api/docs/cities")
        exit(4)
                
        
# Given a filename and an empty variable, store file's content to variable
def load(File=File):
    try:
        with  open(File, "rb") as f:
            prayer_map=pickle.load(f)
            return prayer_map
    except FileNotFoundError:
        return save()
