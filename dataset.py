import datetime
import numpy as np
from datetime import timedelta

def flip(p):
    return 1 if np.random.random() < p else 0

def random_date(start, end):
    """Generate a random datetime between `start` and `end`"""
    return start + datetime.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=np.random.randint(0, int((end - start).total_seconds())),
    )


def random_time(start, hours):
    """Generate a random datetime between `start` and `end`"""
    return (start + datetime.timedelta(
        # Get a random amount of hours
        hours=hours,
    )).time()

def create_positive_test_case(prob = 0.8):
    date_format="%m/%d/%Y %H:%M:%S"
    max_hours = 12
    visits = []
    total_home_hours = 0
    home_lat, home_long = np.random.uniform(0,90), np.random.uniform(0,180)
    coin = flip(prob) 
    while total_home_hours < 30: 
        if coin == 1 :
            end = datetime.datetime.now()
            delta = timedelta(days = 365)
            start = end - delta
            date = random_date(start, end).date() 
            start_time_date = datetime.datetime.strptime("20:00","%H:%M")

            # hours =  np.random.randint(0, max_hours)
            hours = 5
            end_time = random_time(start_time_date, hours )
            start_time = start_time_date.time()
            start_datetime = datetime.datetime.combine(date, 
                              start_time)
            end_datetime = datetime.datetime.combine(date+ timedelta(days=1),
                                end_time)
            total_home_hours += hours
            visit = [home_lat, home_long, start_datetime, end_datetime]
            visits.append(visit)

        else:
            latr, longr = np.random.uniform(0,90), np.random.uniform(0,180)
            end = datetime.datetime.now()
            delta = timedelta(days = 365)
            start = end - delta
            start_datetime = random_date(start, end)
            hours =  np.random.randint(0, max_hours)
            end_datetime=  start_datetime + timedelta(hours=hours)
            visit = [home_lat, home_long, start_datetime, end_datetime]
            visits.append(visit)
    return (visits, (home_lat, home_long), total_home_hours)



def test_case_1():
    start_date1 = datetime.datetime.now().date()
    time1 = datetime.datetime.strptime("1:00","%H:%M").time()
    time2 = datetime.datetime.strptime("8:00", "%H:%M").time()
    start_datetime1 = datetime.datetime.combine(start_date1,
                                time1)
    end_datetime1 = start_datetime1 + timedelta(days=30)
    
    end_date2 = datetime.datetime.now().date()
    end_datetime2 = datetime.datetime.combine(end_date2,
                                time2)
    start_datetime2 = end_datetime2 - timedelta(seconds=3600*12)
    
    return [[1.1, 2.2 , start_datetime2, end_datetime2],
           [12, 42.2 , start_datetime1, end_datetime1]]