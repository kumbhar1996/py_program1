
# Python program to concating two lists 

l1=[10,20,30]
l2=[40,50,60]

# 1.we can concatnate the two list by using (+) operator
print(l1+l2)

# 2. we can concatnate two list by using (*) operator and used a var to store those list we want to concatnate
result=[*l1,*l2]
print(result)

# 3.by using set when in list repeted elements are present

l3=[1,'a']
l4=[1,2,3]

result=list(set(l3+l4))
print(result)

# 4.we can concatnate two list by using extend() 

l5=[10,20,30]
l6=[40,50,60]

l6.extend(l5)
print(l6)