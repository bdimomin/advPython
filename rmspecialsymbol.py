mystring= 'ABc@#$c98PX7al*&ffQWu8fdkl'
print("String before special character remove: {}".format(mystring))
mylist=[]
for i in mystring:
    if i.isalnum():
        mylist.append(i)
normalString="".join(mylist)
print("String after special character remove: {}".format(normalString))