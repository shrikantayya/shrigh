def main():
    a=eval(input("enter the number"))

    while not(a<0):
        print(list((range(a))))
        break

    else:
        print("error")


main()