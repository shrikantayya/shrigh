a=[5,6]
b=eval(input("guess the number"))
l=len(a)
for j in range(0,l+1):
    for i in range(0, 5):
        while(not a==j):
            if(a>b):
                print("given number is smaller")
                break
            if(a<b):
                print("given number is bigger")
                break
        else:
            print("you win")
            break

        b=eval(input("guess the number"))
else:
    print("sry")



