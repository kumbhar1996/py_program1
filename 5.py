
# 5.program for solve the quadratic equation

a=float(input('Enter the value of a: '))
b=float(input('Enter the value of b: '))
c=float(input('Enter the value of c: '))

# a*(x**2)+b*x+c

# roots
x=(-b+(b**2-4*a*c)**0.5)/(2*a)
print(x)

y=(-b-(b**2-4*a*c)**0.5)/(2*a)
print(y)


'''
1.first we give the value of a,b,c by user input
2.we know that quadratic equation (a*(x**2)+(b*x)+c)
3.by using the formulae of root
'''