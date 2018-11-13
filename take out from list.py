a=[1,2,"python","is","-3","3",(1,2,3,4),("rat","cat","mat"),3]
b=len(a)
c=[]
d=[]
e=[]
for i in range(0,b):
    if(isinstance(a[i],int)):
        c.append(a[i])
    if(isinstance(a[i],tuple)):
        e.append(a[i])
    else:
        d.append(a[i])
print(c)
print(d)
print(e)