def prefix_adder(firstlist):
    secondlist=[]
    for i in firstlist:
        if(len(i)>0):
            secondlist.append("Dr."+i)
    return secondlist
firstlist = ["nava","kanth","sdf","eff"]
print(prefix_adder(firstlist))