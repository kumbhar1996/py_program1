
# 13. python program to find the largest among three number

num1=float(input('Enter the first number num1: '))
num2=float(input('Enter the second number num2: '))
num3=float(input('Enter the third number num3: '))

if num1>num2 and num1>num3:
    print('{} number is greter: '.format(num1))
elif num2>num3:
    print('{} number is greter: '.format(num2))
else:
    print('{} number is greter: '.format(num3))

'''
1.by comparing three number we can find the greter number
2.we can use and logical operator
'''