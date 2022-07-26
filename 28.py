
# Python program to find the factors of given number

num=int(input('Enter the number: '))

def factors(num):
    print('Factors of ',num,'are: ')
    for v in range(1,num+1):
        if (num%v)==0:
            print(v,end=',')

factors(num)