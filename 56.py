
# Python program to catch the multiple exception in one line

string=input('Enter str: ')

try:
    num=int(input('Enter the num: '))
    print(string+int)
except (TypeError,ValueError) as e:
    print(e)