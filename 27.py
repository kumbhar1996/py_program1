
# python program to find LCM 

def compute_lcm(x,y):
    if x>y:
        greter=x
    else:
        greter=y

    while(True):
        if((greter%x==0) and (greter%y==0)):
            lcm=greter 
            break
        greter=greter+1
    return lcm
    
num1=12
num2=14

print(compute_lcm(num1,num2))

    