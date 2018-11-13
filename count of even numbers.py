a=eval(input("enter first number"))
b=eval(input("enter second number"))
total=0
for i in range(a,b):
    if(i%2==0):
        total=total+1
print("total number of even numbers is:",total)
