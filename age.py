#!/usr/bin/python
 
# Thiss script calculate age in years, days, hours, minutes and seconds with auto update
# Emad Elsaid's ruby script inspired me to write this script
#ruby script link : https://gist.github.com/blazeeboy/9185583
 
import time, datetime
 
date_of_birth = '1988-4-18'
 
def calc_age(date_of_birth):
    birth_date = date_of_birth.split('-')
    time_now = datetime.datetime.now()
    time_birth = datetime.datetime(int(birth_date[0]),int(birth_date[1]), int(birth_date[2]))
    age = time_now - time_birth
 
    years = age.days//365
    days = age.days%365
    hours = age.seconds//3600
    minutes = (age.seconds//60)%60
    seconds = age.seconds%60
 
    return years, days, hours, minutes, seconds

while True:
    years, days, hours, minutes, seconds = calc_age()
    print years, 'Years', days, 'Days', hours, 'Hours', minutes, 'Minutes', seconds, 'Seconds'
    time.sleep(1)
