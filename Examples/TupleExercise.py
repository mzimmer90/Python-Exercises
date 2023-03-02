MyTuple = ("item1", "item2", "item3", "item4")

for i in MyTuple:
    print("<"+i.center(12)+">")


MyMixTuple = ("item1", "item2", "item3", "item4", "45", "67", "34")
MyList = []
print(MyMixTuple)
for i in MyMixTuple:
    if i.isnumeric():
        print(i)
        MyList.append(int(i))
MySumTup = tuple(MyList)
print(sum(MySumTup))
