a=eval(input("enter the list:"))
b=len(a)
total=0
for i in range(0,b+1):
    if i%10==0:
        total=total+1
print(total)