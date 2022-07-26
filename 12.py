# 12. python program to check year is leapyear

year=int(input('Enter the year: '))

if (year%400==0) and (year%100==0):
    print('Entered year is leap year')
elif (year%4==0) and (year%100!=0):
    print('Entered year is leap year')
else:
    print('Entered number is not leap year')

'''
1.leap year if century year is divisible by 400 and 100 then this is leap year
2.leap year if year is divisible by 4 and not divisible by 100 then this leap year
3.otherwise it is  not leap year