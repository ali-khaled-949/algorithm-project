#Algorithm Project CPSC 335
#Author: Ali Khaled
#Author: Tasin Noor
#Date: 03/18/2024
#Description: This program will

from datetime import datetime, timedelta


def time_to_minutes(my_time_string):  #(COMPLETE)
  time = datetime.strptime(my_time_string, '%H:%M')
  return time.hour * 60 + time.minute


def parse_schedule(schedule):  #(COMPLETE)
  return [(time_to_minutes(start), time_to_minutes(end)) for start, end in schedule]
  


