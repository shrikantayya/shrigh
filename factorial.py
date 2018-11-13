a=eval(input("enter number:"))
if(a<1):
    print("correct number kodo ")
else:
    factorial=1
    for i in range(a,1,-1):
        factorial=factorial*i
    print(factorial)