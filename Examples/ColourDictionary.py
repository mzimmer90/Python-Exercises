MyDict = {"Becci": "Green", "Steve": "Orange", "Melinda": "Purple", "Ryan": "Orange", "Nate": "Purple", "Anna": "Green"}

# Add new entry for Sam
MyDict["Sam"] = "Green"

# Updated existing value for Melinda
MyDict["Melinda"] = "Green"

# MyDict["Sandy"] = "Green"
# del MyDict["Sandy"]

# Remove Sandy with .pop() changing the default False to True since Sandy is not a key in the dictionary yet
MyDict.pop("Sandy", True)

print(MyDict)

# Initialise empty dictionary
colour_counts = {}

# Run through each value of MyDict
for colour in MyDict.values():
    # The colour is initialised with counter 1 when it's found for the first time,
    # and subsequently increased by 1 each time it is found again
    if colour in colour_counts:
        colour_counts[colour] += 1
    else:
        colour_counts[colour] = 1

print(colour_counts)

# Initialise empty new dictionary
NewDict = {}

# Generate NewDict with colours as key and empty list as values.
# Colours are taken from values in MyDict, exploiting set() to get each colour just once
for colour in set(MyDict.values()):
    NewDict[colour] = []

# Iterate through NewDict
for check_colour in NewDict.keys():
    # Iterate through MyDict using both key and value with each iteration
    for name, colour in MyDict.items():
        # Check if the colour (value from MyDict) is different from check_colour (key of NewDict)
        # If true, append the name (key from MyDict) to the value list in NewDict of that colour
        if colour != check_colour:
            NewDict[check_colour].append(name)

# Result will have key colours sorted differently due to creating the keys by using set()
print(NewDict)

