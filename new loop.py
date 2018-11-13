a=5
b=eval(input("guess the number"))
s=7
for i in range(0, 5):
    while(not a==b):

        if(a>b):
            print("given number is smaller")
            break
        elif(a<b):
            print("given number is bigger")
            break
    else:
        print("you win")
        break

    b=eval(input("guess the number"))
else:
    print("your tries over")

for i in range(0, 5):
    b=eval(input("guess the second number"))
    while(not s==b):

        if(s>b):
            print("given number is smaller")
            break
        elif(s<b):
            print("given number is bigger")
            break
    else:
        print("you win")
        break

    b=eval(input("guess the number"))
else:
        print("your tries over")
