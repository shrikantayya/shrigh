a=str(input("enter the word"))
l=list(a)
b=len(l)
v=['a','e','i','o','u']
c=len(v)
e=[]
for i in range(0,b):
    for j in range(0,c):
        if(l[i]==v[j]):
            break
    else:
        e.append(l[i])
print(e)
