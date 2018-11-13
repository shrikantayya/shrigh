a=eval(input("enter the first number:"))
b=eval(input ("enter the second number:"))
for i in range(a,b+1):
    if not(i%2==0):
        print(i)
