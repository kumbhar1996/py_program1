
# check the given string is palindrome or not 

str1=input('Enter the string: ')

str1=str1.casefold()

result=reversed(str1)

if list(str1)==list(result):
    print('string is palindrome')
else:
    print('string is not palindrome')