
# Python program to iterste the items from dictionari by using for loop

d={
    'name':'akshay',
    'loc':'pune',
    'rno':55
}

# if we want to print the both key and value then we use

for k,v in d.items():
    print(k,v)

# if we want to print the keys only then 

for keys in d.keys():
    print(keys)

# if we want to print the values only then 

for values in d.values():
    print(values)