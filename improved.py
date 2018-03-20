from datetime import datetime
from itertools import groupby
import numpy as np
from datetime import timedelta
import math


# Returns a date that is exactly apart from the original date by the specified offset
def date_offset(date, offset):
	return date-timedelta(days=offset)

# returns two lists: locations of visits and total mins spent at eachof these locations
def locations_time(selected):
	locs=[] # List of locations (latitude, longitude)
	total_mins=[] # List of total mins at each selected locations

	for loc, rows in groupby(selected, lambda x: (x[0], x[1])):
		rows= tuple(rows)
		sum1=0.0
		for r in rows:
			sum1+= r[2]
		total_mins.append(sum1)
		locs.append(loc)
	return total_mins, locs




def get_home_location(visits):

	time_format = "%H:%M:%S"
	mins=0.0
	arr_time=datetime.strptime("20:00:00", time_format)
	dep_time=datetime.strptime("08:00:00", time_format)
	selected=[] # List of selected locations to determine Home location 
	for visit in visits:

		# Setting expected arrival and departure dates
		exp_arr = datetime.combine(visit['actual_arrival'].date(),arr_time.time())
		exp_dep = datetime.combine(visit['actual_depart'].date(), dep_time.time())

		# If arrival time is between 12 am - 8 am
		if 4.0 <= (visit['actual_arrival'] - exp_arr).total_seconds()/3600.0 <= 12.0:
			
			exp_arr=date_offset(exp_arr,1)
			mins-= (visit['actual_arrival']- exp_arr).total_seconds()/60.0
		
		# If arrival is between 8pm- 12 am
		elif visit['actual_arrival'] > exp_arr:
			mins-= (visit['actual_arrival']- exp_arr).total_seconds()/60.0
		
		# If departure is between 8pm - 12 am
		if 8.0 <= (exp_dep - visit['actual_depart']).total_seconds()/3600.0 <= 12.0:
			exp_dep = date_offset(exp_dep, -1)
			mins-= (exp_dep - visit['actual_depart']).total_seconds()/60.0

		# If departure is between 12 am - 8 am
		elif exp_dep > visit['actual_depart']:
			mins-= (exp_dep - visit['actual_depart']).total_seconds()/60.0

		# Calculating minutes spent at a locations according to the adjusted dates above
		days = math.ceil((exp_dep- exp_arr).total_seconds()/3600.0/24)
		mins = days*720.0
		selected.append(['%.3f' % visit['latitude'],'%.3f' % visit['longitude'],mins])

	total_mins, locs = locations_time(selected)

	print total_mins

	if max(total_mins) > 1800.0:
		return locs[total_mins.index(max(total_mins))]
	else:
		return "Sorry! We couldn't find Home location for this customer"


