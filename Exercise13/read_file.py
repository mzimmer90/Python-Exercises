with open('pelican.txt', 'r') as pelican:
    lines = pelican.read()
    # llines = pelican.readlines() This doesn't work because pelican.read() already read the content of pelican.txt
    # into memory and the file pointer is at the end of the file. So when .readlines() is called, it reads from the end
    pelican.seek(0)  # this moved the pointer back to the top of the file
    llines = pelican.readlines()

print('The file type of a ".read()" method is', type(lines), "\n")
print('Here is the content of the file:\n')
print(lines)


print('There are', len(llines), 'items in the list using the .readlines() method.\n\nHere is the content of the list:\n')
for i in llines:
    print(i.rstrip("\n"))
# print(''.join(llines)) ".join()" seems the easier option instead of a for loop.
