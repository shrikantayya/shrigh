l1=[1,2,3,4,"abc",5,6,"c"]
a=len(l1)
sum=0
for i in range(0,a+1):
    if isinstance(i,int):
        sum=sum+i


print(sum)
