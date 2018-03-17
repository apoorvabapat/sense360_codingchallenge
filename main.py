from datetime import datetime
from itertools import groupby
import numpy as np
from datetime import timedelta
import math





def get_home_location(visits):
	total=[]
	keys=[]
	date_format = "%m/%d/%Y %H:%M:%S"
	time_format = "%H:%M:%S"
	selected=[]
	selected=[]
	hours=0
	for visit in visits:
		visit[0]='%.3f' % visit[0]
		visit[1]='%.3f' % visit[1]
		
		arr_time=datetime.strptime("20:00:00", time_format)
		dep_time=datetime.strptime("08:00:00", time_format)
		exp_arr = datetime.combine(visit[2].date(),arr_time.time())

		exp_dep = datetime.combine(visit[3].date(), dep_time.time())


		
		
		if (visit[2] - exp_arr).days==-1 and 4 <= ((visit[2] - exp_arr).seconds/3600.0) <=12:
			exp_arr=exp_arr-timedelta(days=1)
			hours-=(visit[2] - exp_arr).seconds/3600.0

		elif visit[2] > exp_arr:
		 	hours-=(visit[2] - exp_arr).seconds/3600.0

		if (exp_dep - visit[3]).days==-1 and 8 <= ((exp_dep-visit[3]).seconds/3600.0) <=12:
			exp_dep=exp_dep+timedelta(days=1)
			hours-= (exp_dep- visit[3]).seconds/3600.0


		elif visit[3] < exp_dep:
			hours-= (exp_dep- visit[3]).seconds/3600.0
		
		diff = visit[3]-visit[2]
		days = math.ceil((exp_dep- exp_arr).total_seconds()/3600.0/24)

		hours=hours + days*12
		
		selected.append([visit[0],visit[1],hours])


	for key, rows in groupby(selected, lambda x: (x[0], x[1])):
		rows= tuple(rows)
		sum1=0.0

		for r in rows:
			sum1+= r[2]
		total.append(sum1)
		keys.append(key)


	if max(total)>=30.0:
		return keys[total.index(max(total))]
	else:
		return "Sorrrry!  Your customer doesn't have a home!"

