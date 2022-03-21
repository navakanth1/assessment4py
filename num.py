def name_adder(firstlist,secondlist):
    for i in firstlist:
        if (len(i)>0):
            secondlist.append(i)
    return secondlist
firstlist = ["a","b"]
secondlist = ["c","d"]
print(name_adder(firstlist,secondlist))