
# 23.python program to find number divisible by another number

num=[10,56,89,10,58,96,100,55,44]

result=list(filter(lambda x:(x%5==0),num))
print(result)