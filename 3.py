
# Python program for find the square root 

num=int(input('Enter the number: '))

result=(num**0.5)
print(result)

'''
Logic of Program

1.initialy we give the user input of any number 
2.we know that sign of squareroot and its power value is 1/2 i.e 0.5
3.we gives the power 0.5 of that number having squareroot find
4.result is stored in result variable
5.print that result
'''

# Another methode of find the squareroot of Real or Complex number

import cmath
num=eval(input('Enter the number: '))
result=cmath.sqrt(num)
print(result)

'''
Logic of program

1.first we import the cmath module for complex number
2.give the user input but here insted of int use eval for solving the string
3.use module cmath.sqrt()
4.where sqrt is function used for find the squareroot of number which may be real or complex
'''