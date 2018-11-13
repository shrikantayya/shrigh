a=eval(input("enter firs numbr"))
b=eval(input("enter secnd number"))
i=0
for i in range(a,b):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)
