def type_adder(firstlist):
    secondlist=[]
    for i in firstlist:
        secondlist.append(type(i))
    return secondlist
firstlist = [3.14,66,"Teddy Bear",True,[],{}]
print(type_adder(firstlist))