
# Calculate the area of triangle

a=float(input('Enter the value of side a: '))
b=float(input('Enter the value of side b: '))
c=float(input('Enter the value of side c: '))

s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(area)

'''
Logic of Program
1.give the three side of traingle a,b,c by user input 
2.number may be in int or float hence use the float
3.first find the perimeter s
4.by using heros formula of area of traingle solve
5.print the result
'''