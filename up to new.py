strl="attending python class on saturday"
str_to_remove="on"
l1=strl.split(' ')
print(l1)
str11=""
if (str_to_remove in l1):
    print("found the str to remove in sentence")
    for idx in l1:
        if(idx !=str_to_remove):
            str11=str11+idx+""
        else:
            break
            #continue
    print(str11)
else:
    print(strl)