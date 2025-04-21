#! /user/bin/env python
"""This code number of days elapsed since the beginning of the year till the given date"""

def is_year_leap(year):
# checks if the year is leap or not
    if year %400 == 0:
        return True
    elif year % 4 == 0:
        if year %100 != 0:
            return True
        else:
            return False
    else:
        return False
#

def days_in_month(year, month):
#
    month_list = [1,2,3,4,5,6,7,8,9,10,11,12]
    days_list = [31,29 if is_year_leap(year)== True else 28,31,30,31,30,31,31,30,31,30,31]
    if month in month_list:
        for mon in range(len(month_list)):
            if  month_list[mon] == month:
                return days_list[mon]
    else:

        return None
#

def day_of_year(year, month, day):
#
    if days_in_month(year,month) != None:
        if day not in range (1,days_in_month(year,month)):
            print("There is no day", day, "in month",month,"of the year",year)
            day_number = ""
            return day_number
        else:
            day_number = 0
            for mon in range (1,month):
                day_number += days_in_month(year,mon)
                #print(mon,day_number)
            day_number += day
            return day_number
    else:
        print("There is no month", month, "in the calendar")
        day_number = ""
        return day_number

if __name__ == "__main__":
    print(day_of_year(2024, 2, 19))
