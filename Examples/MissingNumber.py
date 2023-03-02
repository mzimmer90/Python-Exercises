#Q1

AllNumbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
MissingNumber = {1, 2, 3, 4, 6, 7, 8, 9, 10}

print(AllNumbers-MissingNumber)

NumList = [1, 2, 3, 4, 6, 7, 8, 9, 10]

for i in range(1, 11):
    if i not in NumList:
        print("Missing number is: ", i)

print(AllNumbers.pop())

#Q2

MyTup = (2, 5, 12, 7, 9)

print(max(MyTup) - min(MyTup))

#Q3

MyDict = {"Becci": "Green", "Steve": "Orange", "Melinda": "Purple", "Ryan": "Orange", "Nate": "Green", "Anna": "Green"}
MyDict["Sam"] = "Green"
MyDict["Melinda"] = "Green"
#MyDict["Sandy"] = "Green"
print(MyDict)
#del MyDict["Sandy"]
MyDict.pop("Sandy", True)

print(MyDict)

color_counts = {}
for color in MyDict.values():
    if color in color_counts:
        color_counts[color] += 1
    else:
        color_counts[color] = 1

print(color_counts)
