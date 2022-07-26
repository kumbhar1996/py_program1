
# 18.Python program to find the sum of given number by using fiboneci sequence

num=int(input('Enter the number you have want: '))

n1=0
n2=1

sum=0

while(sum<=num):
    print(sum)
  

    n1=n2
    n2=sum 
    sum=n1+n2
    

'''
Logic of program:

In Fibonacci sequence first two terms are 0 and 1 all other two terms are obtained 
by adding the two preceding terms.

1.First give the integer number as a user input (num)
2.Give the first two number n1,n2 and assign the val for these 0,1
3.create a variable sum and assign the val of these var is 0
4.use the while loop for repeatation and it runs upto until condition is false
5.val of n2 is stored in n1 and val of sum is stored in n2
6.do the addition of n1 and n2 and stored in sum
'''
