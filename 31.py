
# 31.Python program to display the calender

import calendar

year=int(input('Enter the year: '))
month=int(input('Enter the month: '))

result=calendar.month(year,month)
print(result)
